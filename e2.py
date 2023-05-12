import csv
with open("mycsv.csv",'r') as file:
    data=list(csv.reader(file))
print(data)

city= input("Enter City Name")
for row in data:
    if row[0]== city:
        print(row[1])
