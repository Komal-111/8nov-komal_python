#Write a Python program to append text to a file and display the text.
f1=open('k1.txt',"a")
id = input("enter your id:")
stname= input("enter your name ")
city= input ("enter your city name")
f1.write(f"id:{id}\nstname:{stname}\ncity:{city}\n")