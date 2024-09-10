15.Write a Python program to get unique values from a list 

ans :-

numbers = [4, 2, 4, 3, 2, 5, 1, 3]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print("Unique values:", unique_numbers)
