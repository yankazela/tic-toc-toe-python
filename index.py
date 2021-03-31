from math import sqrt, pow

string_one = "My first python code"
string_two = 'A simple print'
string_three = "Using separator"
string_last = string_one + string_three # string concatenation
var = 4

print("********** intro to strings *********")
print(string_one)
print(string_two, "today is:", 17, "of November 2020")
print(string_three, "today", "17th", sep=":") # with separator
print(string_last)
print("love " * 5) # will display "love" five times
print("********** main python operations *********")
var += 8
print(2 + 2, var) #addition
print(round(pow(5, 2)), round(sqrt(9)))

# for loop

for i in range(0, 4):
  print("Print number", i, sep=":")

gre = True
er = 0
while gre:
  re = 1+1

