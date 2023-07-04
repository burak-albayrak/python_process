#Data types

headline = "Hi everyone!!"  #String
price = 300                 #integer
tax = 12.5                  #float

#Get type

print(price)
print(type(headline))

#Syntax

total = price / tax
print(total)

#Assign multpile variables

x, y, z = "apple", 30, 45.6

print(x)
print(y)
print(z)

#Variable change

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Global variables

y = "whaaaat"

def myfunc():
  global y
  y = "boring"

myfunc()

print("Python is " + x)
