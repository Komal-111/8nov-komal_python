#Write a Python function to check whether a number is in a given range
def test_range(n):
    if n in range(1,10):
        print("this is range in")
    else:
        print("not in range .....")
test_range(15)

# second method dynamiclly
n= int(input("enter a number"))
def test_range(n):
    if n in range(1,10):
        print("this is range in")
    else:
        print("not in range .....")
test_range(n)


