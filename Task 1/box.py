import sys


def max_nest(boxes):
    n = len(boxes)

    for i in range(n):
        for j in range(n-i-1):
            if float(boxes[j][0]) < float(boxes[j+1][0]):
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

    dp = [1 for x in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if float(boxes[i][0]) > float(boxes[j][0]) and float(boxes[i][1]) > float(boxes[j][1]) and float(boxes[i][2]) > float(boxes[j][2]):
                dp[j] = max(dp[j], dp[i]+1)

    return dp[n-1]


def take_input():

    testfile = sys.argv[1]
    with open(testfile, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        boxes = [0 for x in range(n)]
        for i in range(1, len(lines)):
            box_dim = lines[i].strip().split()
            boxes[i-1] = box_dim

    print(max_nest(boxes))


take_input()
