#for문

#for (int i = 0; i < 10; i++)
#for i in iterable객체:

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)


for i in range(5, 0, -1):
    print(i, end=" ")
print()

#1부터 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
print(tot)

print(sum(range(1, 11)))

s = "余凖鎬"

for c in s:
    print(c, end=" ")
print()

print(len(s))

for i in range(1,10):
    for a in range(1,10):
        print(f"{i} * {a} = {i * a:<5d}", end=" ")
    print()
    