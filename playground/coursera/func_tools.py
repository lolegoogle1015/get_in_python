from functools import reduce
#reduce() Дозволяє зжимати об'єкт, при цьому запам'ятовуючи результат


def multiply(a, b):
    return a * b

print(reduce(multiply, range(1,6)))


from functools import partial
#partial(func, arg to change) Дозволяє підміняти певні аргументи, цим самим модифікувати поведінку функції


def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)

hier = partial(greeter, greeting = 'Hi')
helloer = partial(greeter, greeting = 'Hello')

print(hier('brother'))
print(helloer('sir'))

#########################$$$Zip func$$$###########################


#zip(list, list) Дозволяє склеїти елементи в обох лістах в кортежі

num_list = range(7)
squared_list = [x ** 2 for x in num_list]

list(zip(num_list, squared_list)) 
