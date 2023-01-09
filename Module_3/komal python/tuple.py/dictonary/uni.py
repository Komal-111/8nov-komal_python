##Write a Python program to print all unique values in a dictionary
d1  = [{"a":"S001"}, {"a": "S002"}, {"ab": "S001"}, {"ab": "S005"}, {"abc":"S005"}, {"a":"S009"},{"VIII":"S007"}]
print("Original List: ",d1)
u_value = set( val for dic in d1 for val in dic.values())
print("Unique Values: ",u_value)


