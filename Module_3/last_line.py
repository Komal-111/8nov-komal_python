#Write a Python program to read last n lines of a file.
f2 = open('k1.txt',"r+")
f2.write("\ nhi komal")
f2.write("\ nhi python")
f2.write("\ nhi reema")
f2.write("\ nhi mera")
f2.write("\ nhi seeta")
f2.write("\ nhi hetal")
print(f2.readlines(1))
print(f2.readlines(23))




'''n=1
for i in f2:
    print(i)
    print(f"Line:{n} = {i}")
    n+=1'''




