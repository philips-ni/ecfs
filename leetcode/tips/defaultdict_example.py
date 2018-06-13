from collections import defaultdict

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]

result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)

print(result)

test = defaultdict(lambda: False)
# test["a"] = False 
if "a" not in test:
    print("not in test")
    print test["a"]
else:
    print("in test")
