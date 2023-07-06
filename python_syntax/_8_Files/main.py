#"r" read, "a" append, "w" write, "x" create

f = open("customers.txt", "r")

print(f.read(30))

f.close()

fileToAppend = open("me.txt", "a")
fileToAppend.write("Burak")
fileToAppend.write("\n")
fileToAppend.write("Albayrak")
fileToAppend.close()

import os
#os.remove("me.txt") dosyayı siler


students = ["Burak", "Hasan", "Sülo"]

file = open("students.txt", "a")

for student in students:
    file.write(student)
    file.write("\n")

file.close()
