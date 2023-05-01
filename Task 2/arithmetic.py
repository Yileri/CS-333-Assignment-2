import sys


def max_value(expr):
    length = (len(expr) + 1) // 2

    min_array = [[0 for i in range(length)] for i in range(length)]
    max_array = [[0 for i in range(length)] for i in range(length)]

    # fill the table for single digit values
    for i in range(length):
        min_array[i][i] = int(expr[2 * i])
        max_array[i][i] = int(expr[2 * i])

    for s in range(length - 1):
        for i in range(length - s - 1):
            # set endpoint for a range
            j = i + s + 1
            min_value = float('inf')
            max_value = float('-inf')

            # check every possible calculation for a specific range
            for k in range(i, j):
                a = calc(min_array[i][k], min_array[k + 1][j], expr[2 * k + 1])
                b = calc(min_array[i][k], max_array[k + 1][j], expr[2 * k + 1])
                c = calc(max_array[i][k], min_array[k + 1][j], expr[2 * k + 1])
                d = calc(max_array[i][k], max_array[k + 1][j], expr[2 * k + 1])
                min_value = min(min_value, min(a, min(b, min(c, d))))
                max_value = max(max_value, max(a, max(b, max(c, d))))

            min_array[i][j] = min_value
            max_array[i][j] = max_value

    return max_array[0][length - 1]


def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return False


def take_input():
    testfile = sys.argv[1]
    with open(testfile, 'r') as file:
        arithmetic = file.read()

    print(max_value(arithmetic))


if __name__ == "__main__":
    take_input()
