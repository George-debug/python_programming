# 1)
# b) Write a module named app.py. When this module is run, it will run in an infinite loop, waiting for inputs from the user.
# The program will convert the input to a number and process it using the function process_item implented in utils.py.
# You will have to import this function in your module. The program stops when the user enters the message "q".

from utils import process_item

if __name__ == '__main__':
    while True:
        x = input('Enter a number: ')
        if x == 'q':
            break
        print(process_item(int(x)))
