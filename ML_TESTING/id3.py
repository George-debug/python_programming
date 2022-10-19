import csv

class Node:
    def __init__(self, yes: int, no: int, lines: set):
        self.yes = yes
        self.no = no

class ID3:

    def __entropy(self, plus, minus):
        if plus == 0 or minus == 0:
            return 0
        else:
            return -plus/(plus+minus)*math.log2(plus/(plus+minus)) - minus/(plus+minus)*math.log2(minus/(plus+minus))

    def __gain(self, root: Node, branches: list[(int, int)]):
        total = root.yes + root.no
        gain = self.__entropy(root.yes, root.no)
        for (plus, minus) in branches:
            gain -= (plus+minus)/total*self.__entropy(plus, minus)
        return gain


    def __train_for(self, root, used_variables):

        max_gain = (-1, -1)

        for i in range(len(self.data[0])-1):
            if used_variables[i]:
                continue

            branches = [(0, 0, []) for i in range(len(self.variable_names[i]))]

            for line in root.lines:
                data_line = self.data[line]

                if data_line[-1] == 0:
                    branches[data_line[i]][0] += 1
                else:
                    branches[data_line[i]][1] += 1

            gain = self.__gain(root, branches)

            if gain > max_gain[0]:
                max_gain = (gain, i)

        if max_gain[0] == -1:
            return None

        used_variables[max_gain[1]] = True







    def __train(self)-> Node:
        used_variables = [False for i in range(len(self.data[0])-1)]


    def __init__(self, data):
        variable_names = [[] for i in range(len(data[0]))]
        variable_values = data[0]
        parsed_data = []

        for i in range(1, len(data)):
            parsed_line = []
            for j in range(len(data[i])):
                if data[i][j] not in variable_names[j]:
                    variable_names[j].append(data[i][j])
                parsed_line.append(variable_names[j].index(data[i][j]))

            parsed_data.append(parsed_line)

        self.variable_names = variable_names
        self.variable_values = variable_values
        self.data = parsed_data


                
                


# csv file to table
def csv_to_table(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        return list(reader)

def main():
    data = csv_to_table("id3_sample.csv")
    id3 = ID3(data)

main()