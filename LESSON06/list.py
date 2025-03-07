# list = ["val", "bob", "mia", "ron", "ned"]

# data = ["Dave", "jane"]

# list.extend(data)

# list.insert(0, "Ayodeji")

# num = [11, 22, 33, 44, 55]

# print(list)
# print(sorted(list, key=str.lower))
# print(list)
# print(num)

# Tuple

tup = tuple(("val", "bob", "mia", "ron", "ned"))
print(type(tup))
newList = list(tup)
print(type(newList))
newList.append("ayodeji")
another = tuple(newList)
print(another)
print(type(another))
