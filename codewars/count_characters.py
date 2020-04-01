#Основна ідея - порахувати всі символи(UTF-8) у строці
##Наприклад стрічка 'aba' return { 'a':2 'b': 1}
###Якщо стрічка пуста - return {}
from collections import Counter
def count(string):
     return Counter(string)

print(count('aaasdasdaagsfhdfgafasd'))
