#System-specific parameters and functions
import sys
#sys.__stdin__ ---використовується для всіх входів, які використовує інтерпретатор, за виключенням скриптів
#sys.__stdout__---використовується для виходів операторів @print@ та expression
#sys.__stderr__
#Схожі до файлових об'єктів, які
# відповідаюьб стандартним входам, виходам та,відповідно, потокам помилок інтерпретатора
#sys.stderr.write('This is stderr text\n')
#sys.stderr.flush()
#sys.stdout.write('This is stdout text\n')
#Список аргументів командної стрічки, які передані скрипту Python
#Перший аргумент, argv[0], має назву аналогічну скрипту Python
#print(sys.argv)

if len(sys.argv) > 1:
    print(float(sys.argv[1])+5)
#Значення настпуного модуля - повний шлях до інтерпретатора Python
#Деякі системи не сприймають цю команду і видають пусту строку з None
##print(sys.executable)
#Дана функція дозволяє розробнику вийти з Пітона. Функція exit приймає
#необов'язковий аргумент, зазвичай ціле число, яке встановлює статус виходу.
#"0" - успішне завершення програми
#"SystemExit" error
