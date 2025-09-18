# remove(x) ==> Removes the first occurrence of value x from the list
# pop([i]) ===> Removes and returns the element at index i (default last elementor -1)

lst = [1, 2, 3, 2]

lst.remove(2)  # removes first 2
print(lst)     # [1, 3, 2]

popped = lst.pop(1)  # removes element at index 1
print(popped)  # 3
print(lst)     # [1, 2]
