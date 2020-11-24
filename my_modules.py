#from collections import deque - модуль для створення черг

#from math import pi

#from math import isnan

#pickle module, json

#import os:
##getcwd - get current working directory
##chdir - change current working directory
##system - run the command in the terminal

#import sys
##argv - parse the command line arguments
##stdin()
##stdout()
##stderr()
##sys.exit()

#import argparse

#import re

#import shutil
##copyfile(dst, src)
##move(dst, src)

#import glob
##glob(search pattern or path)

#import argparse
##ArgumentParser()

############################# Mathematics ############################################

#import math
##math.cos()
##math.log()

#import random
##random.choice() - choose the random element from iterable
##random.sample() - sampling without replacement
##random.random() - gives a random float number
##random.randrange(6) - random integer choosen from range(n)

#import statistics
##statistics.mean()
##statistics.meadian()
##statistics.variance()

############################# Internet Access ############################################
#from urllib.request import urlopen

#smtplib
##smtp.SMTP(hostname) - object for defining the new server
##smtp.SMTP(instance).sendmail('soothsayer@example.org', 'jcaesar@example.org', """email message""")

############################# Dates and Times ############################################

#import datetime
#>>> # dates are easily constructed and formatted
#>>> from datetime import date
#>>> now
#>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
#'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
#>>> birthday = date(1964, 7, 31)
#>>> age = now - birthday
#>>> age.days
