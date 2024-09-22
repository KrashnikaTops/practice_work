#64.Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.  

#ans :-

def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

decimal_numbers = [3.5, 2.1, 5.7, 1.9, 4.3]
max_num, min_num = find_max_min(decimal_numbers)

print("Maximum number:", max_num)
print("Minimum number:", min_num)


