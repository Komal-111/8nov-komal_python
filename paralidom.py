#Write a Python function that checks whether a passed string is 
# or not
str=input("enter a string:  ")
def palindrome_str(str):
    left= len(str)
    if len(str)>=5:
        print("the string is palindrome")
    else:
        print("the string is not  palindrome")
palindrome_str(str)