import csv

with open("python.csv","w",newline="")as f:
        w = csv.writer(f, delimiter=",")
        w.writerow([["Top Gun", "Risky Business", "Minority Report", "Titanic", "The Revenant", "Inception", "Training Day", "Man on Fire", "Flight"]])

