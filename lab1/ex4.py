# camel case to snake case

def camel_to_snake(camel):
    snake = ""
    for c in camel:
        if c.isupper():
            snake += "_"
        snake += c.lower()
    return snake

def main():
    s = input()
    print(camel_to_snake(s))