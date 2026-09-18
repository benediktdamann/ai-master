import csv


with open("data/transactions.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        amount = float(row["amount"])
        if amount > 10000:
            print(row)