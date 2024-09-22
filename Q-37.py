#37.Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

#ans:-

dict = {}

for i in range(1,16):
    dict[i] = i * i
print(dict)    
