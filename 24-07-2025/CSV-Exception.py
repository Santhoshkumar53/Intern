import csv

filename = 'intern.csv'

try:
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        print("Student Details:")
        for row in reader:
            print(f"ID: int{row['ID']}, NAME: {row['Name']}, Email: {row['Email']}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except KeyError as e:
    print(f"Error: Missing column in the file - {e}")
except Exception as e:
    print("An unexpected error occurred:", e)
