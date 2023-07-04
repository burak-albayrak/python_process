#Strings

message_1 = "Hello"
message_2 = 'World'

print(message_1[2:5])
print(message_1[:5])

#len function

print(len(message_2))

#lower & upper

print(message_1.upper())
print(message_2.lower())

#replace

print(message_1.replace("e","o"))

#split & strip

message_3 = "my;name;is;33".strip()

print(message_3.split())
print(message_3.split(";")[3])

#check

txt = "The best things in life are free!"
print("free" in txt)

#format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#input

name = input("Name?")
number = input("Number?")

print(name + number)

#booleans

num = 44
print(bool(num == 43))
