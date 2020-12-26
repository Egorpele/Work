a = int(input())
result = 0
while a != 0:
    if a % 10 == 6 and a % 8 == 0:
        result += a
        a = int(input())
print(a)

