
class Math:
    def sum(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2
    def div(self, num1, num2):
        return num1 / num2
    def mul(self, num1, num2):
        return num1 * num2

math = Math()

num1 = int(input("Please enter the number 1: "))
num2 = int(input("Please enter the number 2: "))
operator = str(input("Please enter the operator(+,-,*,/): "))

if operator == "+":
    print("Result: " + str(math.sum(num1, num2)))
elif operator == "-":
    print("Result: " + str(math.sub(num1, num2)))
elif operator == "*":
    print("Result: " + str(math.mul(num1, num2)))
elif operator == "/":
    print("Result: " + str(math.div(num1, num2)))
else:
    print("Wrong operator!!")


class Person:
    def __init__(self,firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person = Person("Burak", "Albayrak", 22)
print(person.firstName, person.lastName, person.age)


class Worker(Person):
    def __init__(self, salary):
        self.salary = salary

class Customer(Person):
    def __init__(self, creditNumber):
        self.creditNumber = creditNumber
