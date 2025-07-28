import json

# Open and load the JSON file
with open('result.json', 'r') as file:
    data = json.load(file)
print("Name:", data['name'])
print("Degree:", data['Degree'])
print("stream:", data['stream'])
print("college:", data['college'])
print("city:", data['city'])
