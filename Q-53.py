#53.How can you pick a random item from a list or tuple?  

#ans :-In Python, you can use the random module to pick a random item from a list or tuple.

#list:-

import random
list = [11,22,33,44,55,66,77,88,99]
value = random.choice(list)
print(value)

#tuple:-

import random
tuple = (11,22,33,44,55,66,77,88,99)
value= random.choice(tuple)
print(value)


