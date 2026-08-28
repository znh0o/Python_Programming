#연산자

#산술 연산자
a=3
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #나머지
print(a%b) #몫
print(a**b) #제곱

#복합대입 연산자
a += 4
print(a)

a-=10
print(a)

#증감 연산자
#a++
a += 1

#비교연산자
print(3 == 3.0)
print(3 != 4)
print("apple" == "banana")
print(1 < 2 < 3)
print(1<3<2)

#논리연산자
print(True and False)
print(True or False)
print(not True)

#short circuit 테스트
a = 10
b = 0

#print(a/b)

if a > 0 or b > 0:
    print("yes")
else:
    print("no")