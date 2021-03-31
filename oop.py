class Student(object):

  def __init__(self, name, subjects):
    self._name = name
    self._subjects = list(map(lambda x: x, subjects))
  
  def setName (self, name):
    self._name = name
  
  def getName (self):
    return self._name
  
  def addSingleSubject (self, subject):
    self._subjects.append(subject)
  
  def setMarksForSingleSubject (self, subject, marks):
    current = list(filter(lambda x: x['name'] == subject, self._subjects))
    if len(current) > 0:
      print(self._subjects.index(current[0]))
      self._subjects[self._subjects.index(current[0])]["marks"] = marks
  
  def removeSingleSubject(self, subject):
    current = list(filter(lambda x: x['name'] == subject, self._subjects))
    if len(current) > 0:
      self._subjects.pop(self._subjects.index(current[0]))

  def __str__(self):
    print("Name: " + self._name + "\nSubjects: " + " ".join(map(lambda x: str(x['name']) + ": " + str(x['marks']), self._subjects)))

student = Student("Furaha", [{ "name": "Maths", "marks": 98 }, {"name": "English", "marks": 95 }])

student.removeSingleSubject("Maths")
student.addSingleSubject({"name": "French", "marks": 99})
student.setMarksForSingleSubject("French", 100)

student.__str__()

while True:
  1+1