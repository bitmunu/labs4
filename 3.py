def repeated(inp):
    d = {}
    for element in inp:
        if d.get(element, None):
            d[element] += 1
        else:
            d[element] = 1

    return d


print("введите список")
a = list(map(str, input().split()))

mydict = repeated(a)
c = []
a = list(dict.fromkeys(a))

for i in a:
    for key in mydict:
        if i == key:
            c.append(mydict.get(key))

print(' '.join(map(str, c)))
