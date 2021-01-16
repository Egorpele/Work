#1
n = int(input())
a = []
for i in range(n):
    s = float(input)
    if s - int(s) >= 0.5:
        a += [int(s) + 1]
    else:
        a += [int(s)]
print(min(a))
if any(speed > 80 for speed in a ):
    print("Yes")
else:
    print("No")
#2
result = 0
a = int(input())
while a != 0:
    if a%10 == 3:
        result += a
        a = int(input())
print(a)
#3
sum = 0
pCount = 0
oCount = 0
while True:
 n = int(input())
 if n == 0:
   break
 sum += n
 if n > 0:
   pCount += 1
 else:
   oCount += 1
po = pCount - oCount
print('Сумма :',sum)
print('Разность:',po)