from  functools import reduce
sum = 0
l = [[1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]]
new_list = sorted(reduce(lambda x, y: x+y, l))
new_list.reverse()
print(new_list)
for i in range(len(new_list)-1):
    sum += (new_list[i] - new_list[i+1])

print(sum)
#new_new_list = reduce(lambda x, y: x+y, l)
