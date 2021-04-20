import time

n = int(input())
move_list =  input().split()

st = time.time()
x, y = 1, 1

for m in move_list:
    if m == 'L' and y > 1:
        y -= 1
    elif m == 'R' and y < n :
        y += 1
    elif m == 'U' and x > 1 :
        x -= 1
    elif m == 'D' and x < n :
        x += 1
    else:
        #out area
        pass
        print(m)

print(x,y)
