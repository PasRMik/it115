import json

# Create data
person = {
    "name": "Pascal-Ricky",
    "city": "Seattle"
}

# Convert to JSON 
json_string = json.dumps(person)

print(json_string)