#[1,3,5,4,2]라는 리스트를 [5,4,3,2,1]로 만들어보자.
# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

#['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어
#출력해 보자.
# myList = ['Life', 'is', 'too', 'short']
# x = " ".join(myList)
# print(x)
# a = (1,2,3)
# a = a + (4,)
# print(a)

#딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')
# print(result)

#a 리스트에서 중복 숫자를 제거해 보자.
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# a = list(set(a))
# print(a)

# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면
# b 값은 어떻게 될까?
# a = b = [1, 2, 3]
# a[1] = 4
# print(b)
## 정답
# [1, 4, 3]이 출력된다. 
# a와 b 변수는 모두 동일한 [1, 2, 3]이라는 리스트 객체를 가리키고 있었기 때문이다.

# num = int(input())
# result = 0
# i=1
# for i in range(num+1):
#     result = result+i

# print(result)

# a = 0
# while True:
#     a = int(input("종료하려면 -1을 입력하라 : "))
#     if a == -1:
#         break

# print("프로그램 종료")

# while True:
#     print("[메뉴를 입력하세요]")
#     a = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료>>>"))
#     if a == 1:
#         print(end='->')
#         print("게임을 시작합니다.")
#     elif a == 2:
#         print(end='->')
#         print("랭킹보기")
#     elif a == 3:
#         print(end='->')
#         print("게임종료.")
#         break
#     else:
#         print(end='->')
#         print("다시 입력해 주세요.")