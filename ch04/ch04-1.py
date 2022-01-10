## 4-1 상하좌우
## 풀이 일자 2022-01-10
## 시간 13/15 소요
## 정답과는 다소 상이
## 답안 체크 여부 N

n = int(input().split()[0])

plan = input().split()

print(n)

print(plan)

x = 1 #가로
y = 1 #세로
# (y,x)

for move in plan:
    print(move)
    print(y, x)
    if move == 'L' and x > 1:
        x -= 1
    elif move == 'R' and x < n:
        x +=1
    elif move == 'U' and y > 1:
        y -=1
    elif move == 'D' and y < n:
        y +=1

print(str(y)+' '+str(x))
