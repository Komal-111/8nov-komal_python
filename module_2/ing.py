#Write a Python program to add 'ing' at the end of a given string (length 
#ld be at least 3). If the given string already ends with 'ing' then add 
#'ly' instead if the string length of the given string is less than 3, leave i
str=" i am komal"
print(str)
a=str.replace('l','ing')
print(a)
if str.len()>3:
    print(str.replace('ing','ly'))
else:
    print("not  print....")
