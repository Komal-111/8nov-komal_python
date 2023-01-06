#Write a Python program to replace last value of tuples in a list

compart = ('keyboard','mouse','monitor','cpu','harddisk')
print(compart)
a = list(compart)
a[4] = 'joystick'
compart=tuple(a)
print(a)