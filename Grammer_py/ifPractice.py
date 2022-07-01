a = True

if a:
    print("택시를")
    print("타고")
    print("가라")

money = 1000
card = True

if money >= 1500 or card:
    print("버스를 타고 가라")
else:
    print("걸어라")

print('a' in ('a', 'b', 'c')) #True
print('j' not in 'python') #True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어라")

#조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket2 = ['paper', 'money', 'cellphone']
if 'money' in pocket2:
    pass
else:
    print("카드를 꺼내라")

if money >= 1500:
    print("버스를 타고 가라")
elif card:
    print("버스를 타고 가라")
else:
    print("걸어라")