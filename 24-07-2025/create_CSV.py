import csv

with open('Intern.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Email',])
    writer.writerow(['01', 'Santhosh Kumar G', 'santhosh.doodle.com'])
    writer.writerow(['02', 'krishna', 'Krishna.doodle'])
    writer.writerow(['03', 'Jake', 'Jake.doodle']) 
