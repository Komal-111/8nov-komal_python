# Write a Python program to remove an empty tuple(s) from a list of tuples. 
tuple =[(), (0,1,2,3),(6,7,8)]
tuple = [t for t in tuple if t]
print(tuple)

'''L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)'''