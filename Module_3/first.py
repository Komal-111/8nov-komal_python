#Write a Python program to read an entire text file.
f1= open("k1.txt", "r+")
print(f1.readlines())
f1.write(" hi students")
f1.write(" hi python")
f1.write(" hi komal")
f1.write(" hi reema")
f1.close()