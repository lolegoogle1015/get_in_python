#Функція, яка приймає 2 числові аргументи, які задають довжину масиву
##Функція повертає числа з цього проміжку, які мають таку властивість 135 = 1^1 + 3^2 + 5^3
###Якщо таких чисел немає в цьому проміжку - вона повертає пустий список
def filter_fuc(a):
    return sum(int(d) ** (i+1) for i,d in enumerate(str(a))) == a

def sum_dig_pow(a,b):
    return filter(filter_func, range(a, b+1))
