# No, because tuples are immutable

tup = (4, 5, 6, "anas", "roorkee")

tup[1] = 99

print(tup)  # TypeError: 'tuple' object does not support item assignment
