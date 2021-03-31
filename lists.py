myList = [8, 2, 3, 5, 6, 10, 11, 55, 83, -1, 6]

second = myList + []

# myList.extend([45, 60, -9])

lastElementRemoved = myList.pop()
second.append(30)

myList.insert(7, 33)

for x in range(67):
  if(x in second):
    print("found element ", x, 'in position ', second.index(x))

#removed
print('removed', lastElementRemoved)

#display elements
for i in range(len(myList)):
  print('Element number ', i, ':', myList[i])

print('******************')

for y in range(len(second)):
  print('Element number ', y, ':', second[y])

print('******************')
print(myList == second)

print('test in, ', 3 in myList)

#sub-list from index 3 to 7
print (myList[2:8])


while True:
  1+1