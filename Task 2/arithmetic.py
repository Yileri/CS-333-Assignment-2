import sys

def max_value(expression):


def take_input():

    testfile = sys.argv[1]
    with open(testfile,'r') as file:
        arithmetic = file.read()

    print(arithmetic)

take_input()
