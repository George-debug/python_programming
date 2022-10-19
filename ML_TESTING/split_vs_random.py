import math
import random

class Problem:
    def __init__(self, a, b):
        self.yes = a
        self.no = b

    def get_entropy_of(self, a, b):
        if a == 0 or b == 0:
            return 0
        else:
            return -a/(a+b) * math.log2(a/(a+b)) - b/(a+b) * math.log2(b/(a+b))


    def get_information_gain_if(self, a, b):
        prob_left = (a+b)/(self.yes+self.no)
        prob_right = 1 - prob_left

        entropy_left = self.get_entropy_of(a, b)
        entropy_right = self.get_entropy_of(self.yes-a, self.no-b)

        return self.get_entropy_of(self.yes, self.no) - prob_left*entropy_left - prob_right*entropy_right


p = Problem(40, 40)

g = [
    [30, 10],
    [25, 15],
    [5, 35],
    [20, 10],
    [20, 20],
    [15, 10]
]

for i in range(len(g)):
    print("Information gain if split on feature", i, "is", p.get_information_gain_if(g[i][0], g[i][1]))
    
