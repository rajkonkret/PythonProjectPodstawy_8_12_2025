# csv - dane oddzielone znakiem podziału, " ", ";", "," , "|", ":", "tab"
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
import csv

row = ['radek', 'coe', "3", 0]
fields = ['name', 'branch', 'year', 'row']

dict_name = dict(zip(fields, row))
print(dict_name)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'row': 0}

filename = "records.csv"

with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = "records_dict.csv"
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dict_name)

products = [
    {"sku": 1, "exp_date": 'today', "price": 200},
    {"sku": 2, "exp_date": 'today', "price": 200},
    {"sku": 3, "exp_date": 'tomorrow', "price": 200},
    {"sku": 4, "exp_date": 'today', "price": 200},
    {"sku": 5, "exp_date": 'tomorrow', "price": 200},
    {"sku": 6, "exp_date": 'today', "price": 200},
]

list_product = [key for key in products[0]]
print(list_product)  # ['sku', 'exp_date', 'price']

filename = "records_discount.csv"
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=list_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)  # writerows
