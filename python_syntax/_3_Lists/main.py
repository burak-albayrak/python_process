#list

students = ["suleyman", "mehmet", "mahmut"]
print(students)

students.append("ciko")
print(students)

students.remove("mehmet")
print(students)

print(len(students))

#list constructor

cities = list(("Angara","İzmir","Ankara"))

print(str(cities.count("Ankara")))
print(str(cities.index("İzmir")))
cities.pop(0)
print(cities)
cities.insert(0,"İstanbul")
print(cities)
cities.reverse()
print(cities)

#tuples
#list ile benzer sadece elemanlar değiştirilemez bu yüzden daha performanslıdır

tuple_list = ("Hi",1,5,7,(2,3,4))

#sets
#index'siz ve sırasız elemanlardan oluşur, veri tekrarı olmaz

set_list = {"Ahmet", "Burak", "Albayrak"}

#set union

SetA = {1,2,3,4,5}
SetB = {1,6,7,8,9}

print(SetA | SetB)
print(SetA.union(SetB))
print(SetB.union(SetA))

print(SetA & SetB)
print(SetA.intersection(SetB))
print(SetB.intersection(SetA))

print(SetA - SetB)
print(SetA.difference(SetB))
print(SetB.difference(SetA))

print(SetA ^ SetB)
print(SetA.symmetric_difference(SetB))
print(SetB.symmetric_difference(SetA))

#Dictionary

dictionary = {
    "book" : "kitap",
    "table" : "masa"
}
print(dictionary)

dictionary_2 = dict(kitap = "book", masa = "table")
print(dictionary_2)

dictionary["book"] = "kitap111"
del(dictionary["table"])
print(dictionary)
