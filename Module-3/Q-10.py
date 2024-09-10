10.Write a python program to generate and a list of first and last 5 elements where the values are square of numbers between 1 and 30.

ans :-

square=[x**2 for x in range(1,31)]
print("frist 5 elements:",square[:5])
print("last 5 elements:",square[-5:])

