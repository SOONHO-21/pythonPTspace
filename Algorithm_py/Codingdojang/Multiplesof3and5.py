from unittest import result

result = 0
for i in range(1000):
    if i%3 == 0 or i%5 ==0:
        result = result+i

print(result)

set3 = set(range(3, 1000, 3))
set5 = set(range(5, 1000, 5))

print(sum(set3 | set5))