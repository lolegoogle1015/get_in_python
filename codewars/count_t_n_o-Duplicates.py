#Функція, яка повертає кількість символів, які повторюються в стрічці
##Вхідна стрічка складається тільки з букв алфавіту(верхнього та нижнього регістру)
from collections import Counter
def duplicate_count(text):
    sum = 0
    for k, v in Counter(text.casefold()).items():
        if v > 1:
            sum+=1
    return sum
     
