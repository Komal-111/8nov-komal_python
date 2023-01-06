#Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.
#Sample data: {'1': ['a','b'], '2': ['c','d]
a = {}
n = int (input("number of element"))
for i in range(n):
    k = input("enter key:")
    v = input("enter value:")
    a.update({k:v})
   
   
print(a) 