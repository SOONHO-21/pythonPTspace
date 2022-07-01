# a = [1, 2, 3, ['a', 'b', 'c']]
# print(a[3][0]) #print a
# print(a[-1][1]) #print b
# a = [1,2,['a','b',['Life', 'is']]]
# print(a[2][0]) #print a
# print(a[2][2][1])
# a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(a[2:5]) #print [3, ['a', 'b', 'c'], 4]
# print(a[3][:2]) #print ['a', 'b']

a = [1, 2, 3]
print(str(a[1]) + 'Hi') #2Hi
a.append(4) #리스트 요소 추가
print(a)
a.append([5,6]) #리스트에 리스트 추가
print(a)
a.append('asdf') #리스트 안에는 어떤 자료형도 추가할 수 있다.
print(a)
a.extend([7,8,9]) #리스트에 여러 요소 추가
print(a)