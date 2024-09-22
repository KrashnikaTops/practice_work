#9.Write a Python function that takes two lists and returns true if they have at least one common member.

#ans :-


def mylist(list1,list2):
    for item in list1,list2:
        return True
    
list1 = [1,2,3,4,5]    
list2 = [5,6,7,8,9]

print(mylist(list1,list2))
