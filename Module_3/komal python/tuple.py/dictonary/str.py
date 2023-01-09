#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string: 'w3resource'
#Expected output:
#{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
s = input ("enter string")
dic = {}
for ch in s:
    if ch in dic:
        dic[ch]+=1
    else:
        dic[ch]=1
for key in dic:
    print(key,':',dic[key])
print("My dic",dic)
