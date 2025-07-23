dict1 = {"one": 11, "two": 22, "three": 33, "four": 44, "five": 55}
keys = ["one", "two"]
d2 = {}
for key in keys:
    if key in dict1:
        d2[key] = dict1[key]
print(d2)