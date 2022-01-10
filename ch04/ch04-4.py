"""
게임개발
ch04 -04.py
제한시간 40분
"""

n, m = map(int, input().split())
x, y, d = map(int, input().split())

print(n,m)
print(x,y,d)
maps= []

for i in range(n):
    maps.append(list(map(int, input().split())))

print(maps)