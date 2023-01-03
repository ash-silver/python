import sys
input = sys.stdin.readline

global w, h, p, q, t, x, y, cnt
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

cnt, x, y = 0, p, q

# def xIndexOut():
#     if x >= p :
#         return False
#     else :
#         return True

# def yIndexOut():
#     if y >= q:
#         return False
#     else:
#         return True

def indexOut():
    if x >= p or y >= q or x <= 0 or y <= 0:
        return True
    else:
        return False

def end():
    if cnt == t:
        return str(x) + " " + str(y)

def rightUp() :
    global w, h, p, q, t, x, y, cnt
    x += 1
    y += 1
    cnt += 1
    end()
    if indexOut() == True :
        x -= 1
        y += 1
        if indexOut() == False:
            x += 1
            y -= 1
            return leftUp()
        else : 
            return rightDown()

def leftDown() :
    global w, h, p, q, t, x, y, cnt
    x -= 1
    y -= 1
    cnt += 1
    end()
    if indexOut() == True:
        x -= 1
        y += 1
        if indexOut() == False:
            x += 1
            y -= 1
            return leftUp()
        else :
            return rightDown()


def rightDown():
    global w, h, p, q, t, x, y, cnt
    x += 1
    y -= 1
    cnt += 1
    end()
    if indexOut() == True:
        x += 1
        y += 1
        if indexOut() == False:
            x -= 1
            y -= 1
            return rightUp()
        else : 
            return leftDown()

def leftUp():
    global w, h, p, q, t, x, y, cnt
    x -= 1
    y += 1
    cnt += 1
    end()
    if indexOut() == True:
        x -= 1
        y -= 1
        if indexOut() == False:
            x += 1
            y += 1
            return leftDown()
        else :
            return rightUp()

print(rightUp())