#Write a Python program to map two lists into a dictionary 
stddata = {"id ", "name ", "sub",  "city"  } 
stddata1 = {"101 ", "komal ", "python",  "rajkot"  } 

print (stddata)
keys = ['id','name','sub','city']
values= ['101','komal','python','rajkot']
stddata = dict(zip(keys,values))

print (stddata)
 