import numpy as np
from Ratio import Ratio
from read_data import csv_to_table, table_to_float, table_to_points


def list_to_point_string(l: list) -> str:
    rv = "("
    for val in l:
        rv += f"{val}, "

    return rv[:-2] + ")"


def euclidian_distance(self, v1: list, v2: list) -> tuple[float, str]:
    text = f"d({list_to_point_string(v1)}, {list_to_point_string(v2)}) = "
    text += "√("
    for i in range(len(v1)):
        text += f"({v1[i]} - {v2[i]})^2 + "
    text = text[:-3]
    text += ") = √("

    power_array = np.power(np.array(v1) - np.array(v2), 2)
    for i in range(len(power_array)):
        text += f"{power_array[i]} + "
    text = text[:-3]
    text += ") = √("
    sumed = np.sum(power_array)
    rv = np.sqrt(sumed)
    text += f"{sumed}) = √{sumed} = {rv}"

    return rv, text


class Knn:
    def __init__(self, data: list[list], k):
        self.data = data
        self.k = k

    distance = euclidian_distance

    def classify(self, point: list) -> tuple[float, str]:
        distances = [0] * len(self.data)
        text = ""

        for i in range(len(self.data)):
            distances[i], aux = self.distance(self.data[i][:-1], point)
            text += aux + "\n\n"

        args = np.argsort(distances)
        text += f"Closest {self.k} points:\n"
        for i in range(self.k):
            text += f"{self.data[args[i]]}\n"

        return np.mean([self.data[i][-1] for i in args[:self.k]]), text


def leave_one_out(data: list[list], k: int) -> tuple[Ratio, str]:
    text = ""
    errors = 0
    for i in range(len(data)):
        knn = Knn(data[:i] + data[i + 1:], k)
        classification, aux = knn.classify(data[i][:-1])
        classification = round(classification)
        text += f"Point {data[i]} classified as {classification}\n"
        text += f"Real value: {data[i][-1]}\n"
        text += aux + "\n\n\n"

        if abs(classification - data[i][-1]) > 0.0001:
            errors += 1

    return Ratio(errors, len(data)), text


ex17_data = table_to_float(csv_to_table("ex17_data.csv")[1:])
print("data: ", ex17_data)

error_rate, text = leave_one_out(ex17_data, 1)

# open file to write
f = open("ex17.txt", "w", encoding="utf-8")

f.write(text)
f.write("\n\n\n")
f.write(f"Error rate: {error_rate}")
