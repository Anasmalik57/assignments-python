# Use append() to add a single element at the end
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# Use insert(index, element) to add at a specific position
my_list.insert(1, 10)
print(my_list)  # [1, 10, 2, 3, 4]

# Use extend() to add multiple elements from another list
my_list.extend([5, 6])
print(my_list)  # [1, 10, 2, 3, 4, 5, 6]
