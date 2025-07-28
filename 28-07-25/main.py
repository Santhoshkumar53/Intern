import json
person = {
    "name": "Santhosh",
    'Degree': "B.tech",
    'stream': "CSE",
    'college': "Crescent",
    "city": "Chennai"
}
with open('out.json', 'w') as file:
    json.dump(person, file, indent=4)  
