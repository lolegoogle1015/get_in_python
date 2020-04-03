"""f = open('filename', mode)
f = open('filename', 'w')

text_modes = ['r', 'w', 'a', 'r+']
binary_modes = ['br', 'bw', 'ba', 'br+']"""

#####################File Methods#######################

f.write('Data')
f.read() #it reads as much as it can
f.tell()
f.seek()
f.readline()
f.readlines()#return splited by '\n' list
f.close()
