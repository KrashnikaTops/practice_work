3. Differentiate between append () and extend () methods? append ()

ans :-

append()

list1 = [1, 2, 3]
list1.append(4)
print(list1)  # Output: [1, 2, 3, 4]

list1.append([5, 6])
print(list1)  # Output: [1, 2, 3, 4, [5, 6]]

Extend ()

list1 = [1, 2, 3]
list1.extend([4, 5])
print(list1)  # Output: [1, 2, 3, 4, 5]

list1.extend((6, 7))
print(list1)  # Output: [1, 2, 3, 4, 5, 6, 7]

