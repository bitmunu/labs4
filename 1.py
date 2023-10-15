print("введите список")
a = list(map(int, input().split()))

maximum = a[0]
x = 0

minimum = a[0]
c = 0

for i in range(1, len(a)):

    if a[i] > maximum:
        maximum = a[i]
        x = i

    if a[i] < minimum:
        minimum = a[i]
        c = i

for i in range(1, len(a)):

    if a[i] == maximum:
        a[i], a[c] = a[c], a[i]

print(' '.join(map(str, a)))
