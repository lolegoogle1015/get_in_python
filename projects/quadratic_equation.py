#Програма, яка запускається з командної стрічки з параметрами
##Вираховує значення коренів квадратного рівняння та виводить їх в консоль
###На вхід програмі подаються коефіцієнти a b c
####В консоль повинні виводитись два корені квадратного рівняння
import sys
from math import sqrt

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


#a * x^2 + b * x + c = 0

D = pow(b, 2) - (4*a*c)

if D > 0:
    xa = (-b + sqrt(D))/(2*a)
    xb = (-b - sqrt(D))/(2*a)
    print(xa)
    print(xb)
elif D == 0:
    xa = xb = -(b/(2*a))
    print(xa)
    print(xb)
else:
    print("There are no roots")
