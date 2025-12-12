import csv

filename = "records.csv"
# filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "

    csv_f.seek(0)  # powrót na poczatek pliku
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    # csvreader = csv.reader(csv_f, delimiter=";")

    print(csvreader)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

    print("Fields:", fields)
    print("Rows:", rows)
