#Write a Python program to find the second smallest number in a list. 
list1= ['45','55','75','80','90']
largest =len (list1)
def find_len(list1):
    length=len(list1)
    list1.sort()
    print("second largest number is",list1 [length -2])