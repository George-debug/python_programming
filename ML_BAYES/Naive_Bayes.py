# delete when done
import csv
from Ratio import Ratio

class NaiveBayes:
    def __init__(self, data):
        self.variable_names = data[0][:-1]
        self.end_variable_name = data[0][-1]
        self.variable_values_names = [[] for i in range(0, len(data[0])-1)]
        self.end_variable_values_names = []
        self.data = []
        
        for i in range(1, len(data)):
            data_line = []
            

            for j in range(0, len(data[i])-1):
                if data[i][j] not in self.variable_values_names[j]:
                    self.variable_values_names[j].append(data[i][j])
                data_line.append(self.variable_values_names[j].index(data[i][j]))

            if data[i][-1] not in self.end_variable_values_names:
                self.end_variable_values_names.append(data[i][-1])
            data_end_variable = self.end_variable_values_names.index(data[i][-1])

            self.data.append((data_line, data_end_variable))

        self.likelihood, self.end_variable_probability, self.variable_value_probability = self.__get_probabilities()

    def __get_probabilities(self):
        # matrix likelihood[end_variable][variable][value] = {0}
        likelihood = [[[0 for _ in range(len(self.variable_values_names[i]))] for i in range(len(self.variable_names))] for _ in range(len(self.end_variable_values_names))]
        variable_value_probability = [[0 for _ in range(len(self.variable_values_names[i]))] for i in range(len(self.variable_names))]
        end_variable_counter = [0 for _ in range(len(self.end_variable_values_names))]


        for data_line in self.data:
            variable_data, end_variable_data = data_line

            for i in range(len(variable_data)):
                likelihood[end_variable_data][i][variable_data[i]] += 1
                variable_value_probability[i][variable_data[i]] += 1
            
            end_variable_counter[end_variable_data] += 1

        for likelihood_line_index in range(len(likelihood)):
            for variable_index in range(len(likelihood[likelihood_line_index])):
                likelihood_variable = likelihood[likelihood_line_index][variable_index]
                for i in range(len(likelihood_variable)):
                    likelihood_variable[i] = Ratio(likelihood_variable[i], end_variable_counter[likelihood_line_index])
        
        for variable_index in range(len(variable_value_probability)):
            for i in range(len(variable_value_probability[variable_index])):
                variable_value_probability[variable_index][i] = Ratio(variable_value_probability[variable_index][i], len(self.data))

        sum_end_variable_counter = sum(end_variable_counter)

        for i in range(len(end_variable_counter)):
            end_variable_counter[i] = Ratio(end_variable_counter[i], sum_end_variable_counter)

        return likelihood, end_variable_counter, variable_value_probability

    def __product_of_contitionaly_probabilities(self, variable_values, end_variable_index) -> Ratio:
        product = Ratio(1, 1)
        as_function = ""
        as_ratio = ""

        for i in range(len(variable_values)):
            product *= self.likelihood[end_variable_index][i][variable_values[i]]
            as_function += "P(" + self.variable_names[i] + " = " + self.variable_values_names[i][variable_values[i]] + " | " + self.end_variable_name + " = " + self.end_variable_values_names[end_variable_index] + ") * "
            as_ratio += str(self.likelihood[end_variable_index][i][variable_values[i]]) + " * "

        as_function = as_function[:-3]
        as_ratio = as_ratio[:-3]

        return product, as_function, as_ratio

    def __product_of_probabilities(self, variable_values) -> Ratio:
        product = Ratio(1, 1)
        as_function = ""
        as_ratio = ""
        
        for i in range(len(variable_values)):
            product *= self.variable_value_probability[i][variable_values[i]]
            as_function += "P(" + self.variable_names[i] + " = " + self.variable_values_names[i][variable_values[i]] + ") * "
            as_ratio += str(self.variable_value_probability[i][variable_values[i]]) + " * "

        as_function = as_function[:-3]
        as_ratio = as_ratio[:-3]
        return product, as_function , as_ratio


    def predict(self, line) -> str:
        variable_values = [self.variable_values_names[i].index(line[i]) for i in range(len(line))]
        end_probabilities = []
        product_of_probabilities, text_as_function, text_as_ratio = self.__product_of_probabilities(variable_values)
        product_of_probabilities.simplify()
        
        rv = "P(X) = P("
        for i in range(len(variable_values)):
            rv += self.variable_names[i] + " = " + self.variable_values_names[i][variable_values[i]] + ", "
        rv = rv[:-2] + ") =\n       " + text_as_function + " =\n       " + text_as_ratio + " =\n       " + str(product_of_probabilities) + "\n\n"

        for i in range(len(self.end_variable_values_names)):
            product_of_contitionaly_probabilities, text_as_function, text_as_ratio = self.__product_of_contitionaly_probabilities(variable_values, i)
            product_of_contitionaly_probabilities.simplify()
            end_probabilities.append(product_of_contitionaly_probabilities * self.end_variable_probability[i])
            end_probabilities[i].simplify()
            rv += "P(" + self.end_variable_name + " = " + self.end_variable_values_names[i] + " | X) =\n       P(" + self.end_variable_name + " = " + self.end_variable_values_names[i] + " | "
            for j in range(len(variable_values)):
                rv += self.variable_names[j] + " = " + self.variable_values_names[j][variable_values[j]] + ", "
            rv = rv[:-2] + ") =\n       " + text_as_function + " * P(" + self.end_variable_name + " = " + self.end_variable_values_names[i] + ") =\n       " + text_as_ratio + " * " + str(self.end_variable_probability[i]) + " =\n       " + str(product_of_contitionaly_probabilities) + " * " + str(self.end_variable_probability[i]) + " =\n       " + str(end_probabilities[i]) + "\n\n"

        answer = self.end_variable_values_names[end_probabilities.index(max(end_probabilities))]

        rv += "Sum of all probabilities = " + str(sum(end_probabilities).get_simplified()) + "\n\n"

        for i in range(len(end_probabilities)):
            rv += "P(" + self.end_variable_name + " = " + self.end_variable_values_names[i] + " | X) = " + str(end_probabilities[i]) + "\n"

        rv += "\n" + self.end_variable_name + " = " + answer + "\n\n"

        return answer, rv

    def __str__(self):
        rv = ""

        for i in range(len(self.end_variable_values_names)):
            rv += "P(" + self.end_variable_name + " = " + self.end_variable_values_names[i] + ") = " + str(self.end_variable_probability[i]) + "\n"

        for i in range(len(self.variable_names)):
            for j in range(len(self.variable_values_names[i])):
                rv += "P(" + self.variable_names[i] + " = " + self.variable_values_names[i][j] + ") = " + str(self.variable_value_probability[i][j]) + "\n"

        for i in range(len(self.end_variable_values_names)):
            for j in range(len(self.variable_names)):
                for k in range(len(self.variable_values_names[j])):
                    rv += "P(" + self.variable_names[j] + " = " + self.variable_values_names[j][k] + " | " + self.end_variable_name + " = " + self.end_variable_values_names[i] + ") = " + str(self.likelihood[i][j][k]) + "\n"

        return rv

def csv_to_table(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        return list(reader)

def main():
    data = csv_to_table("data26.csv")

    nb = NaiveBayes(data)
    print(nb)
    test27 = ["Sunny","Cool", "High", "Strong"]
    solution, steps = nb.predict(test27)
    print(steps)
    print(solution)

main()