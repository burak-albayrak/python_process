print("Welcome to factorial calculator!")
number = int(input("Please enter a number: "))

result = 1

while number != 1:
    result = result * number
    number = number -1

print("Result is: ", result)
