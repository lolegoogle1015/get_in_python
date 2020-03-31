#pass
for i in range(100):
    pass

#break
result = 0
while True:
    result +=1
    if result >= 100:
        break
print(result)

for i in range(10):
    if i == 5:
        break
    print(i)

#continue
result = 0

for i in range(10):
    if i % 2 != 0:
        continue
    result += i
print(result)
