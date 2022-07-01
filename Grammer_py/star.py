#별 찍기 - 직각삼각형
# i=0
# result = ''
# for i in range(1, 6):
#     result = '*'*i
#     print(result)

# print()

#별 찍기 - 역직각삼각형
# i=0
# result = ''
# for i in range(5, 0, -1):
#     result = '*'*i
#     print(result)

# print("")

# i=0
# result = ''
# for i in range(1,6):
#     result = '*'*(6-i)
#     print(result)

# print()

#또 다른 방법 - reversed 내장함수 이용
# i=0
# result = ''
# for i in reversed(range(1,6)):
#     result = '*'*i
#     print(result)

#왼쪽 방향으로 직각삼각형 찍기
# result= ''
# for i in range(1,6):
#     result = ' '*(5-i) + '*'*i
#     print(result)

# for i in range(0,5):
#     result = ' '*i + '*'*(5-i)
#     print(result)

for i in range(1,6):
    result = ' '*(i-1) + '*'*(6-i)
    print(result)