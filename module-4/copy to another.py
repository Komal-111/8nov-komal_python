#Write a Python program to copy the contents of a file to another file



with open('komu.txt','r') as firstfile, open('first.txt','a') as secondfile:
	
	
	for line in firstfile:
			
			
			secondfile.write(line)
