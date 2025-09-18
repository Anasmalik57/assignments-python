word = "PanaJi@12256"


print(sum(map(str.islower, word))) # 4
print(sum(map(str.isupper, word))) # 2
print(sum(map(str.isnumeric, word))) # 2

