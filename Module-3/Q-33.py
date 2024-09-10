33.write a python script to concatenate following dictionaries to create a new one.

ans:-

d1={'x':1,'y':2}
d2={'z':1,'y':4}
d3={'k':5}
d4={}
for d in (d1,d2,d3):d4.update(d)
print(d4)
