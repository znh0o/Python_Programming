#반복문 : while문 , for문

#while문
#1~10까지 반복 출력

i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("End")

nums = [1,3,4,5]
target = 2
i = 0

while i < len(nums):
    if nums[i] == target:
        print("찾았다")
        break
    i += 1
else:
    print("못찾았다")

#1~10까지의 합
i=1
tot = 0
while i <= 10:
    tot += i
    i += 1
print(tot)

