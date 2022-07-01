# import imp
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price_soldier(3)

# import imp
# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

# from theater_module import price_soldier as price
# price(5)

# 패키지 파트
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

#혹은
# from travel import thailand
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

#클래스를 import하는 방법
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#__all__
# from travel import *    #특정 패키지나 모튤명을 import하지 않음
#                         #__all__에다가 모듈명을 넣어줘야 함
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


#예외 처리 파트
#from multiprocessing.sharedctypes import Value

# try:
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력 : ")))
#     nums.append(int(input("두 번째 숫자를 입력 : ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0}/{1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 값을 잘 못 입력")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력 : "))
#     num2 = int(input("두 번째 숫자를 입력 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError as err:
#     print(err)

#사용자 정의 예외 처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력 : "))
#     num2 = int(input("두 번째 숫자를 입력 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError as err:
#     print(err)
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)

from traceback import print_tb


a = {'일본', '중국', '한국'}
a.add('베트남')
a.add('중국')
a.remove('일본')
a.update({'홍콩', '한국', '태국'})
print(a)