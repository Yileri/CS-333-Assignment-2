import sys

def maxNest(boxes):
    n = len(boxes)

    for i in range(n):
        for j in range(n-i-1):
            if boxes[j][0] < boxes[j+1][0]:
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

    dp = [1 for x in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1] and boxes[i][2] < boxes[j][2]:
                dp[j] = max(dp[j], dp[i]+1)

    return max(dp)

def take_input():
    #n = int(input())
    #boxes = [0 for x in range(n)]

    #for i in range(n):
    #    box_dim = input().split(" ")
    #    boxes[i] = box_dim
    #print(boxes)

    testfile = sys.argv[1]
    with open(testfile, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
