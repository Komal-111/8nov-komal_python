#Write a Python function that takes two lists and returns true if they have 
#at least one common member.

def common_data(list1,list2):
    result= False
    for x in list1:
        for y in list2:
            if x  == y:
                result=True
                return result
print("my list1" ,common_data([1,2,3,4,5,6,7],[1,2,5,6,7,8,9]))
print("my list2" ,common_data([11,12,13,15],[0,1,2,3]))