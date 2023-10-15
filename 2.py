print("введите список")
a = list(map(int, input().split()))

print("введите список")
b = list(map(int, input().split()))

c = []

for i in range(len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]:
            c.append(a[i])
            break

print(' '.join(map(str, set(c))))
