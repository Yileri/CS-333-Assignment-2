import sys


def max_nest(boxes):
    n = len(boxes)

    for i in range(n):
        for j in range(n-i-1):
            if float(boxes[j][0]) < float(boxes[j+1][0]):
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

    print("*" * 100)
    print(boxes)

    dp = [1 for x in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1] and boxes[i][2] < boxes[j][2]:
                dp[j] = max(dp[j], dp[i]+1)

    return max(dp)


def take_input():

    # testfile = sys.argv[1]
    with open('test1.txt', 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        boxes = [0 for x in range(n)]
        for i in range(1, len(lines)):
            box_dim = lines[i].strip().split()
            boxes[i-1] = box_dim

    print(boxes)
    print(max_nest(boxes))


take_input()
