#32. Write a Python script to sort (ascending and descending) a dictionary by value. 

#ans:-

Dict = {'a':11,'b':15,'c':17,'d':5,'e':6,'f':8,'g':19}

dict1 = sorted(Dict.values())
print("Ascending order : ",dict1)

dict1.reverse()
print("Desending order : ",dict1)


