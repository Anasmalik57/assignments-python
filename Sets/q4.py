# 1-> remove(x) → removes x, raises error if x not present.
# 2-> discard(x) → removes x if present, no error if missing.
# 3-> pop() → removes a random element (because sets are unordered).


s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

s.discard(5)  # no error
print(s)  # {1, 3}

s.pop()
print(s)  # one element removed randomly
