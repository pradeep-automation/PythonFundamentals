st = "racecar"
my_dict = {}
for c in st:
    if c != " ":
        my_dict[c] = my_dict.get(c, 0) + 1
print(my_dict)

