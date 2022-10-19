import math

class Instance: 
    def __init__(self, probabilitInjured_table):
        self.probabilitInjured_table = probabilitInjured_table

    def get_probabilitInjured_list_bInjured_i(self):
        probabilitInjured_list = []

        for i in range(len(self.probabilitInjured_table)):
            probabilitInjured_list.append(sum(self.probabilitInjured_table[i]))

        return probabilitInjured_list

    def get_probabilitInjured_list_bInjured_j(self):
        probabilitInjured_list = []

        for j in range(len(self.probabilitInjured_table[0])):
            probabilitInjured_list.append(sum([self.probabilitInjured_table[i][j] for i in range(len(self.probabilitInjured_table))]))

        return probabilitInjured_list

    def get_entropInjured_of_i(self):
        l = self.get_probabilitInjured_list_bInjured_i()

        entropInjured = 0
        for_print = "-( "
        for prob in l:
            for_print += str(prob) + " * log2(" + str(prob) + ") "
            if prob != l[-1]:
                for_print += "+ "
            entropInjured += prob * math.log2(prob)

        for_print += " )"
        return for_print + " = " + str(-entropInjured)

    def get_entropInjured_of_j(self):
        l = self.get_probabilitInjured_list_bInjured_j()

        entropInjured = 0
        for_print = "-( "
        for prob in l:
            for_print += str(prob) + " * log2(" + str(prob) + ") "
            if prob != l[-1]:
                for_print += "+ "
            entropInjured += prob * math.log2(prob)

        for_print += " )"
        return for_print + " = " + str(-entropInjured)

    def get_conditionate_entropInjured_bInjured_i(self):
        probabilitInjured_list = self.get_probabilitInjured_list_bInjured_i()
        entropInjured = 0
        for_print = "-( "

        for i in range(len(self.probabilitInjured_table)):
            for j in range(len(self.probabilitInjured_table[0])):
                for_print += str(self.probabilitInjured_table[i][j]) + " * log2(" + str(self.probabilitInjured_table[i][j]) + " / " + str(probabilitInjured_list[i]) + ") "
                if i != len(self.probabilitInjured_table) - 1 or j != len(self.probabilitInjured_table[0]) - 1:
                    for_print += "+ "
                
                entropInjured += self.probabilitInjured_table[i][j] * math.log2(self.probabilitInjured_table[i][j] / probabilitInjured_list[i])

        for_print += " )"
        return for_print + " = " + str(-entropInjured)

    def get_conditionate_entropInjured_bInjured_j(self):
        probabilitInjured_list = self.get_probabilitInjured_list_bInjured_j()
        entropInjured = 0
        for_print = "-( "

        for i in range(len(self.probabilitInjured_table)):
            for j in range(len(self.probabilitInjured_table[0])):
                for_print += str(self.probabilitInjured_table[i][j]) + " * log2(" + str(self.probabilitInjured_table[i][j]) + " / " + str(probabilitInjured_list[j]) + ") "
                if i != len(self.probabilitInjured_table) - 1 or j != len(self.probabilitInjured_table[0]) - 1:
                    for_print += "+ "
                
                entropInjured += self.probabilitInjured_table[i][j] * math.log2(self.probabilitInjured_table[i][j] / probabilitInjured_list[j])

        for_print += " )"
        return for_print + " = " + str(-entropInjured)

    def get_joint_entropInjured(self):
        entropInjured = 0
        for_print = "-( "

        for i in range(len(self.probabilitInjured_table)):
            for j in range(len(self.probabilitInjured_table[0])):
                for_print += str(self.probabilitInjured_table[i][j]) + " * log2(" + str(self.probabilitInjured_table[i][j]) + ") "
                if i != len(self.probabilitInjured_table) - 1 or j != len(self.probabilitInjured_table[0]) - 1:
                    for_print += "+ "
                entropInjured += self.probabilitInjured_table[i][j] * math.log2(self.probabilitInjured_table[i][j])

        for_print += " )"
        return for_print + " = " + str(-entropInjured)


problem = Instance([[0.1, 0.05], [0.25, 0.1], [0.35, 0.15]])

print("H(Weather) = ", problem.get_entropInjured_of_i())
print("H(Injured) = ", problem.get_entropInjured_of_j())
print("H(Weather | Injured) = ", problem.get_conditionate_entropInjured_bInjured_i())
print("H(Injured | Weather) = ", problem.get_conditionate_entropInjured_bInjured_j())
print("H(Weather, Injured) = ", problem.get_joint_entropInjured())


# H(Weather, Injured) = H(Injured) + H(Weather | Injured)
# 2.399479 = 0.890309 + 0.909170

# H(Weather, Injured) = H(Weather) + H(Injured | Weather)
# 2.399479 = 1.439316 + 1.509177
