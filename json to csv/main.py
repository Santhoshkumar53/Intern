import json
import csv

with open('data.json', 'r') as file:
    data = json.load(file)
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)  
    writer.writerow(data.keys())

    writer.writerow(data.values())

print("Data written to output.csv")
