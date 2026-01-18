import csv

data = [
    ["Name", "Age"],
    ["Ali", 25],
    ["Ahmed", 30]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
