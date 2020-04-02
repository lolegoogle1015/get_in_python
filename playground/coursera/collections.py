###################################################



                #List methods


empty_list = []
empty_list = list()

none_list = [None] * 10

print(none_list)

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
    ['Elena', 4.4],
    ['Andriy', 4.2]
]

print(len(collections))

"""collections.append("OrderedDict")"""
#extends your list with another elements
"""collections.extend()"""
#Мінімальне значення
"""collections.min()"""
#Максимальне
"""collections.max()"""
#сумує
"""collections.sum()"""
#Можна форматувати масив за допомогою цього метода
"""print(" ,".join(collections))"""
#Сортує, але не повертає відсортований список
"""list.sort(reverse = True/False)"""
#Сортує та повертає список
"""sorted(list, reverse = True/False)"""
#Реверсить елементи в списку
"""reversed(numbers)"""
#Повертає індекс (переданого в якості аргумента) елемента
"""index("елемент")"""
#Додає елемент на певній позиції
"""insert()"""
#Видаляє всі елементи зі списку
"""clear()"""
#Повертає копію списку
"""copy()"""
#Повертає кількість елементів == аргументу
"""count(елемент)"""
#Видаляє елемент на певнй позиції
"""pop()"""
#Видаляє перший елемент == аргументу
"""remove(елемент)"""

#########################################################


                #Tuple methods


#Кортежі - незмінні

"""empty_tuple = ()"""
"""empty_tuple = tuple()"""

"""immutables = (int, str, tuple)"""
"""immutables[0] = float """#TypeError

"""
blink = ([], [])
blink[0].append(0)#Буде працювати, бо змінюємо не кортеж, а елемент

Піддаються хешуванню
hash(tuple())
"""

#count()
#index()

########################################################



                #Dict methods



#del dict('Key')
#dict.setdefault('key', 'default')
#items()
#values()
#keys()
#get()


"""from collections import OrderedDict
Створює об'єкт словника, який буде атоматично сортувати всі елементи у словнику
ordered = OrderedDict()

for n in range(10):
    ordered[n] = str(n)

for k in ordered:
    print(k)
"""




#######################################################################



                #Set methods



empty_set = set()
number_set = {1,2,3,4,5,6}

print(number_set)

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set)
print(even_set)

union_set = odd_set | even_set
print(union_set)
union_set = odd_set.union(even_set)
print(union_set)

intersection_set = odd_set & even_set
print(intersection_set)
intersection_set = odd_set.intersection(even_set)
print(intersection_set)

difference_set = odd_set - even_set
print(difference_set)
difference_set = odd_set.difference(even_set)
print(difference_set)


symmetric_difference_set = odd_set ^ even_set
print(symmetric_difference_set)
symmetric_difference_set = odd_set.symmetric_difference(even_set)
print(symmetric_difference_set)

#set.remove(element)
#set.pop()

#Незмінна версія множини
frozen = frozenset(['Anna', 'Elsa', "Kristoff"])
