import csv
with open('./Resources/budget_data.csv', 'rt') as csvfile:
    total_months = -1
    total = 0
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        total_months = total_months + 1
        if row[1].isdigit():
            print (int(row[1]))
            total += int(row[1])
        else:
            0
        print (row)

print ("Financial Analysis ")
print ("---------------------------- ")
print (f"Total Months: {total_months}")
print (f"Total: {total}")