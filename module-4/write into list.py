# Write a Python program to write a list to a file. 
city = ['rajkot','broda','jamnagar','surat']
with open('2.txt',"w") as fp:
    for  items in city:
    
        fp.write("%s\n" % items)
    print("done")
list = city
print(list)
