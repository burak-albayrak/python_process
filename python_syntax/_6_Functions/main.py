def SayHi(name = "Guest", surname = " Surname"):
    print("Hello " + name + surname)

SayHi()
SayHi("Burak")
SayHi("Burak ", "Albayrak")

def dikUcgenAlani(a,b):
    return a * b / 2

area = dikUcgenAlani(5,10)
print(area)

#Lambda

dikUcgenAlani2 = lambda a,b : a * b / 2
area2 = dikUcgenAlani2(6,10)
print(area2)
