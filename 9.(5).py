f = open("C:\\Users\\Administrator\\Desktop\\mahammad.txt", 'r')
data = f.read()
lw = data.split()
d = {}
for word in lw:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)
