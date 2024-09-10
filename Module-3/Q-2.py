2. How will you remove last object from a list? 
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

ans:- Using pop() method:-

list1 = [2, 33, 222, 14, 25]
last_item = list1.pop() 
# Removes and returns the last item
print(last_item) # Output: 25
print(list1)      # Output: [2, 33, 222, 14]


Using del statement:-

list1 = [2, 33, 222, 14, 25]
del list1[-1]  # Deletes the last item
print(list1)   # Output: [2, 33, 222, 14]

Regarding  list[-1].  :-

list1 = [2, 33, 222, 14, 25]
print( list1[-1])


