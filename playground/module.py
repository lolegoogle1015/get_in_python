from  mypackage.utils import *
#не рекомендується, тому що він не явний
import this, inspect, os

print(inspect.getfile(this))
print(os.listdir("/usr/lib/python3.6"))

if __name__ == '__main__':
    print(multiply(2,3))
