# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다.", treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4.Quit
# Enter Number: """

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

coffee = 10
while True:
    money = int(input())
    if money == 300:
        print("돈을 받았으니 커피를 줍니다.")
        coffee = coffee - 1
        print("남은 커피의 양 : %d잔" % coffee)
    elif money > 300:
        print("돈을 받았으니 커피를 줍니다.")
        print("잔액 : %d" % (money - 300))
        coffee = coffee - 1
        print("남은 커피의 양 : %d잔" % coffee)
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양 : %d잔" % coffee)
    if coffee == 0:
        print("품절")
        break

#1부터 10까지의 숫자 중에서 짝수만 출력
a = 0
while a < 10:
    a = a+1
    if a%2 != 0:
        continue
    print(a)
#continue문은 while문의 맨 처음(조건문: a<10)으로 돌아가게 하는 명령어