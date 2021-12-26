import csv

rows=[]
fields=[]

with open("noble_prize.csv",'r') as f:
    data_record =csv.reader(f)
    fields=next(data_record)
    print(type(data_record))
    for row in data_record:
        print(row)
        rows.append(row)
    print(data_record.line_num)
    print(data_record.__sizeof__())

print(fields)
print(rows[0:2])