#Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

d1 ={ 'a': 100, 'b': 200 , 'c': 300}
d2 ={ 'a':300, 'b':200, 'd':400 }
d3 = {}
for i,j in d1.items():
    for x,y in d2.items():
        if i == x:
            d3[i]= (j+y)
    
print("my new dictionary", d3)
d3 = {'a' : 400,'b':400 , 'd': 400 ,'c': 300}
print("final dictionary" ,d3)
