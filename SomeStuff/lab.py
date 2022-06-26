tasks_4_dvsn = []
a = []
c = []
for i in range(1, 21):
    a.append(i)

print(a)
a = a[19::-1]
print(a)
b = a[0]
print(b)

for i in a:
    if b % i == 0:
        c.append((b,i))
print(c)
print(type(c[1]))

