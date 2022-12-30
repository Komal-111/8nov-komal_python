# FACTORIAL NUMBER PROGRAMME
num=int(input("ENTER  A NUMBER :"))
factorial=1
if num < 0:
   print("this number is not factorial ")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
