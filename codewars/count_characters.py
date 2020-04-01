#Основна ідея - порахувати всі символи(UTF-8) у строці
##Наприклад стрічка 'aba' return { 'a':2 'b': 1}
###Якщо стрічка пуста - return {}
def count(string):
    if len(string) == 0:
        return {}
    return {i: string.count(i) for i in string }

print(count('aa'))
