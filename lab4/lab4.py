import os
from typing import Callable
# 1)    Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’


def get_unique_extension(path: str):
    extension_set = set()
    for file in os.listdir(path):
        extension = os.path.splitext(file)[1][1:]
        if extension != '':
            extension_set.add(extension)

    extension = list(extension_set)
    return sorted(extension)


# print(get_unique_extension('C:\\Users\\George\\Desktop'))


# 2)    Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

def write_files_with_A(path: str, write_file: str):
    with open(write_file, 'w') as f:
        for file in os.listdir(path):
            if file[0] == 'A' or file[0] == 'a':
                f.write(os.path.join(path, file) + '\n')


# write_files_with_A("C:\\Users\\George\\Desktop",
#                    "D:\\Python Programming\\lab4\\files_with_a.txt")


# 3)    Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count,
# unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie.
# Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.

def tail_20(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()[-20:]


def count_extension(path: str) -> list[tuple[str, int]]:
    extension_set = {}
    for file in os.listdir(path):
        extension = os.path.splitext(file)[1][1:]
        if extension in extension_set:
            extension_set[extension] += 1
        else:
            extension_set[extension] = 1

    return sorted(extension_set.items(), key=lambda x: x[1], reverse=True)


def ex3(my_path: str):
    if os.path.isfile(my_path):
        return tail_20(my_path)

    return count_extension(my_path)


# print(ex3("D:\\Python Programming\\lab4\\files_with_a.txt"))
# print(ex3("C:\\Users\\George\\Desktop"))


# 4)    Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv).
# Lista trebuie să fie sortată crescător.

# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.

def ex4() -> list[str]:
    path = input("Path: ")
    return get_unique_extension(path)


# print(ex4())


# 5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere,
# target și to_search și returneaza o listă de fișiere care conțin to_search.
# Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv
# iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
# Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.

def search_recursive(target: str, to_search: str) -> list[str]:
    file_list = []
    if os.path.isfile(target):
        with open(target, 'rb') as file:
            if to_search in file.read():
                file_list.append(target)
    else:
        for file in os.listdir(target):
            file_list += search_recursive(os.path.join(target,
                                          file), to_search)

    return file_list


def ex5(target: str, to_search: str):
    if not os.path.exists(target):
        raise ValueError(f"Despre ce path vorbim? \"{target}\"?")

    return search_recursive(target, bytes(to_search, 'utf-8'))


# print(ex5("D:\\Python Programming\\lab4\\files_with_a.txt", "a"))
# try:
#     print(ex5("C:\\Users\\George\\Desktop\\Cocktail Vault", "cocktail"))
# except ValueError as e:
#     print(e)


# 6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru în plus:
# o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor,
# se va apela funcția respectivă cu instanța excepției ca parametru.

def my_callback(e: Exception):
    print(e)


def ex6(target: str, to_search: str, callback: Callable[[Exception], None]) -> list[str]:
    if not os.path.exists(target):
        callback(ValueError(f"Despre ce path vorbim? \"{target}\"?"))
        return []

    try:
        return search_recursive(target, bytes(to_search, 'utf-8'))
    except Exception as e:
        callback(e)
        return []


print(ex6("C:\\Users\\George\\Desktop\\Cocktail Vault", "lemon", my_callback))


# 7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar cu
# următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului
# (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.

def ex7(file_path: str) -> dict:
    return {
        "full_path": os.path.abspath(file_path),
        "file_size": os.path.getsize(file_path),
        "file_extension": os.path.splitext(file_path)[1][1:],
        "can_read": os.access(file_path, os.R_OK),
        "can_write": os.access(file_path, os.W_OK)
    }


# print(ex7(".\\files_with_a.txt"))


# 8)	Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc.
# Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
# Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]

# Calea "C:\\director" are pe disc următoarea structură:

# C:\\director\\fisier1.txt <- fișier

# C:\\director\\fisier2.txt <- fișier

# C:\\director\\director1 <- director

# C:\\director\\director2 <- director

def ex8(path: str) -> list[str]:
    file_list = []
    for file in os.listdir(path):
        file_list.append(os.path.join(path, file))

    return file_list


# print(ex8("C:\\Users\\George\\Desktop\\Cocktail Vault"))
