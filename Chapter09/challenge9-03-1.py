import csv

with open("python.csv", "r")as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(", ".join(row))
