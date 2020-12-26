n = int(input())
result = 0
for i in range(n):
    a = int(input())
    if a % 10 == 2 and a % 3 == 0:
        result += 1
print(result)

