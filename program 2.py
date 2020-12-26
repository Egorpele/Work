a = int(input())
result = 0
while a != 0:
    if a % 10 == 4 and a % 6 == 0:
        result += a
        a = int(input())
print(a)
