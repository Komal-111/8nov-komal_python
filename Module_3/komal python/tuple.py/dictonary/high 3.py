#Write a Python program to find the highest 3 values in a dictionary# Python program to demonstrate
# finding 3 highest values in a Dictionary

from collections import Counter


my_dict = {'A': 67, 'B': 23, 'C': 45,
		'D': 56, 'E': 12, 'F': 69}

k = Counter(my_dict)


high = k.most_common(3)

print("Initial Dictionary:")
print(my_dict, "\n")


print("Dictionary with 3 highest values:")
print("Keys: Values")

for i in high:
	print(i[0]," :",i[1]," ")
