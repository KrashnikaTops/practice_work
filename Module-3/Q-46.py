46.Write a Python program to combine values in python list of dictionaries. 
   Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]  
 
ans :-

from collections import defaultdict

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
combined = defaultdict(int)

for entry in data:
    combined[entry['item']] += entry['amount']

result = [{'item': item, 'amount': amount} for item, amount in combined.items()]
print(result)
