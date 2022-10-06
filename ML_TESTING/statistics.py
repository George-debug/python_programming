import random

# exec(open("statistics.py").read()) to run this file

def decision(probability):
    return random.random() < probability

class boolean_event_list:
    __test_number = 10000

    def __init__(self, *probabilities):
        self.__probabilities = list(probabilities)

    def generate_event(self):
        return map(decision, self.__probabilities)

    def __any_happens(self) -> bool:
        return any(self.generate_event())

    def any_happens(self):
        return sum(self.__any_happens() for _ in range(self.__test_number)) / self.__test_number

    def __exactly_n_happens(self, n) -> bool:
        return sum(self.generate_event()) == n

    def exactly_n_happens(self, n):
        return sum(self.__exactly_n_happens(n) for _ in range(self.__test_number)) / self.__test_number



