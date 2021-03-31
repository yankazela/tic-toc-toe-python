data = ["John,Bolt,52", "Furaha,Kazadi,87", "Nene,Winny,70"]

maxMarks = 0
students = []

for line in data:
  item = line.split(',')
  maxMarks =  int(item[2]) if int(item[2]) > maxMarks else maxMarks
  students.append({
    "firstname": item[0],
    "surname": item[1],
    "marks": int(item[2])
  })
  

for student in students:
  if student['marks'] == maxMarks:
    print(student['firstname'] + ' ', student['surname'] + ' ', student['marks'])

gameGrid = [[0 for i in range(3)] for j in range(3)]
gameGrid[2][2] = 3

print('game grid', gameGrid[2][2])


while True:
  1+1