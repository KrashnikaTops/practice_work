32. Write a Python script to sort (ascending and descending) a dictionary by value. 

ans:-

import operator
d={1: 2,3: 4,4:3,2:1,0:0}
print('original dictioary:',d)
sort=sorted(d.items(),key=operator.itemgetter(0))
print('assending value:',sort)
sorted_d=sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print('descending value:',sort)

