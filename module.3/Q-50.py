#50.Write a Python function to check whether a number is perfect or not.  

#ans:-

n = 28
divisors = 0
for i in range(1, n):
    if n % i == 0:
        divisors += i
if divisors == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

