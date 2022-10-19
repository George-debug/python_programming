from math import log2

class Node:
    def __init__(self, children):
        self.__children = children

    def get_child(self, i):
        return self.__children[i]

    def get_children(self):
        return self.__children

class Leaf:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


def table_to_tree(table: list|float) -> Node|Leaf:
    if isinstance(table, float):
        return Leaf(table)
    else:
        return Node([table_to_tree(row) for row in table])




class DecisionCompass:
    def __init__(self, table):
        self.__root = table_to_tree(table)

    def __print_tree(self, tree, output = ""):
        if isinstance(tree, Leaf):
            print(output + "  ==>  " + str(tree.get_value()))
        else:
            for i, child in enumerate(tree.get_children()):
                self.__print_tree(child, output + "  " + str(i))

    def print_tree(self):
        self.__print_tree(self.__root)

    def __get_probabilities_of(self, tree, level) -> list[float]:
        if isinstance(tree.get_child(0), Leaf):
            return [x.get_value() for x in tree.get_children()]

        if level == 0:
            return [sum(self.__get_probabilities_of(x, level + 1)) for x in tree.get_children()]

        ziped = zip(*[self.__get_probabilities_of(x, level + 1) for x in tree.get_children()])

        return [sum(x) for x in ziped]

    def get_probabilities(self, level) -> list[float]:
        return self.__get_probabilities_of(self.__root, level)


    def __get_entropy_of(self, tree, level) -> float:
        probabilities = self.__get_probabilities_of(tree, level)

        return -sum([x * log2(x) for x in probabilities if x != 0])

    def get_entropy(self, level) -> float:
        return self.__get_entropy_of(self.__root, level)

    # function for p(level1, level2)
    def __get_joint_probability_of(self, tree, level1, level2) -> list[list[float]]:
        if level1 == 0:
            return [self.__get_probabilities_of(x, level2) for x in tree.get_children()]

        return [self.__get_joint_probability_of(x, level1 - 1, level2) for x in tree.get_children()]

    def get_joint_probability(self, level1, level2) -> list[list[float]]:
        if level1 == level2:
            return self.get_probabilities(level1)
        elif level1 > level2:
            aux = level1
            level1 = level2
            level2 = aux

        return self.__get_joint_probability_of(self.__root, level1, level2)


def main():
    table = [[0.1, 0.05], [0.25, 0.10], [0.35, 0.15]]
    compass = DecisionCompass(table)
    compass.print_tree()

    names = ["Weather", "Injured"]

    for i in range(len(names)):
        probabilities = [round(x, 6) for x in compass.get_probabilities(i)]
        print("P(" + names[i] + ") = " + str(probabilities))

        entropy = round(compass.get_entropy(i), 6)
        print("H(" + names[i] + ") = " + str(entropy))

        for j in range(len(names)):
            if i != j:
                # conditional_entropy = round(compass.get_conditional_entropy(i, j), 6)
                # print("H(" + names[i] + " | " + names[j] + ") = " + str(conditional_entropy))

                joined_probabilities = compass.get_joint_probability(i, j)

                print("P(" + names[i] + ", " + names[j] + ") = " + str(joined_probabilities))
                

main()