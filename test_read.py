import csv
with open("recipients.csv", newline="", encoding="utf-8")as f:
    reader=csv.DictReader(f)
    for row in reader :
        print(row["email"])