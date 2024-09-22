#38. Write a Python program to check multiple keys exists in a dictionary 

#ans:-
dict = {"Name":"krashnika","age":21,"city":"bharuch","roll no":12}

dict1 = ["Name","city"]

key = all(dict)
for keys in dict1:
    if keys not in dict:
        key = False
print(f"All exists keys is {key}.")
