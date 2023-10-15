print("введите список")
a = list(map(int, input().split()))
c = []

for i in range(len(a)):
    c.append([])

    for j in range(len(a)):
        if a[j] > a[i]:
            c[i].append(a[j])

    if len(c[i]) == 0:
        print(f"Больше, чем {a[i]} элементов нет")
    elif len(c[i]) > 0:
        print(f"Больше, чем {a[i]}: {', '.join(map(str, c[i]))}")
    else:
        c.pop()
