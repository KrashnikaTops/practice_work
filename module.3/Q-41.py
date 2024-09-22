#41. Write a Python program to combine two dictionary adding values for common keys. 
 #   d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
  #  Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

# ans:-


d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400} 

dict = d1.copy()

for key,values in d2.items():
    if key in dict:
        dict[key] += values
    else:
        dict[key] = values    
print(dict)     

