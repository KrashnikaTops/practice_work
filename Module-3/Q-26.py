26.Write a Python program to replace last value of tuples in a list.


ans :-

list=[(10,20,30),(40,50,60),(70,80,90)]
print(list)
print([tuple[:-1]+(100,200)for tuple in list])
