#29.Write a Python program to unzip a list of tuples into individual lists. 

#ans:-

list1= [(1,4),(2,5),(3,6)]
print(list(zip(*list1)))
