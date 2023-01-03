import sys
input = sys.stdin.readline

global xLocation, yLocation, direction, gDo
seroSize, garoSize  = map(int, input().split())
xLocation, yLocation, direction = map(int, input().split())

gDo = [0] * seroSize
clean, rotateCnt = 0, 0

for i in range(0, seroSize):
    gDo[i] = list(map(int, input().split()))

def rotate():
    if direction == 0:
        direction = 3
    else :
        direction -= 1


        