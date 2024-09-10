45.write a Python program to find the highest 3 values in a dictionary  

ans :-

dict = {
    'o': 101,
    'p': 105,
    'q': 80,
    'r': 200,
    's': 905,
    't': 90
}
h_values = sorted(dict.values(), reverse=True)[:3]
print("The highest 3 values are:", h_values)


