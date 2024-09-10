51. Write a Python function that checks whether a passed string is palindrome or not  

ans:-

def palindrome_che(str):
    rev=''.join(reversed(str))  
    if(str==rev):
        print("string is palindrome")
    else:
        print("string is not palindrome")
num=input("Enter the string ")
palindrome_che(num)
