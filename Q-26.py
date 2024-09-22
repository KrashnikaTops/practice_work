#26.Write a Python program to replace last value of tuples in a list.


#ans :-

list=[(10,20,30),(40,50,60),(70,80,90)]
print(list)
print([tuple[:-1]+(100,200)for tuple in list])



Tuple_list = [(1,2,3),(4,5,6),(7,8,9)]

new_value = 100

Updated_list = [t[:-1] + (new_value,) for t in Tuple_list]
print(Updated_list) 
