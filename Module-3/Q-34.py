34.write a python script to check if a given key already exists in a dictionary.

ans:-

my_dict = {1:10,2:20,3:30}
key_to_check = 20
if key_to_check in my_dict:
    print("Key exists")
else:
    print("Key does not exist")