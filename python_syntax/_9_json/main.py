import json

data = '{"firstName":"burak","lastName":"albayrak"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName":"samet",
    "email":"blablabla.com"
}

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("samet"))
