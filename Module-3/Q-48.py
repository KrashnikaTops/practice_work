48.Write a Python function to calculate the factorial of a number (a nonnegative integer)  


ans:-

def fac(num):
    fac=1
    if num<0:
        print("not exit for negative number")
    elif num==0:
        print(" factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            fac = fac * i
        print(" factorial of",num,"is",fac)
n=int(input("Enter the number "))
fac(n)

