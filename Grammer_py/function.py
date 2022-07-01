import random

def getRandomNumber():
    number = random.randint(1,10)   #1~10 까지의 숫자 중 랜덤한 정수 출력
    return number

print(getRandomNumber())