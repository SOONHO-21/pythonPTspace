import math

m = int(input())

n = int(input())
if n == 0:
    print("입력 다시하라.")
    n = int(input())

if m > n:
    print(math.ceil(m/n))
else:
    print(1)