#Write a Python program to remove duplicates from a list.
mylist= ['mango','banana','apple','orange','mango']
print(mylist)
mylist= list(dict.fromkeys(mylist))
print(mylist)
