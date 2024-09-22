#35. How Do You Traverse Through A Dictionary Object In Python? 

#ans:-

#for key in dict:
     #print(key)

#for value in dict.values():
     #print(value)


dict = {"Name":"Krashnika","age":21,"city":"Bharuch","roll no":12}

for key,value in dict.items():
    print(f"{key}:{value}")
