dictionOne = {
  "name": "yannick",
  "age": 33,
  "married": True
}

dictionOne.pop("married")

print(list(dictionOne.keys()))

for key in dictionOne:
  print(key, ': ', dictionOne[key])

for key in list(dictionOne.keys()):
  print(key, ': ', dictionOne[key])

x = None if dictionOne.get("married", None) == None else dictionOne.get("married")

print(x)


while True:
  1+1