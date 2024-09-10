11.Write a Python function that takes a list and returns a new list with unique elements of the first list. 

ans :-

def unique_element(input_list):
    return list(set(input_list))
original_list=[1,2,3,3,2,4,5,6,6,5,4]
unique_list=unique_element(original_list)
print(unique_list)

