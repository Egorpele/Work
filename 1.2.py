#1
m = 0
n = int(input())
for i in range(0, n):
    k = int(input())
    if (k % 4 == 0) and (k > m):
        m = k
print(m)
#2
n = int(input())
k = 0
for i in range(int(n)):
    a = input()
    if int(a) % 10 == 3:
        k += 1
print("Количество: ", k)
#3
m = 0
n = int(input())
for i in range(0, n):
    k = int(input())
    if (k % 3 == 0) and (k < m):
        m = k
print(m)
#4
n = int(input())
result = 0
for i in range(n):
    a = int(input())
    if a % 10 == 2 and a % 7 == 0:
        result += 1
print(result)
#5
n = int(input())
result = 0
for i in range(n):
    a = int(input())
    if a % 10 == 2 and a % 6 == 0:
        result += 1
print(result)
#ТЕСТЫ
# 1.ДЕДА 2.6  3.4  4.6  5.12  6.10  7.127