# display both 
import os
import csv

csvpath = os.path.join('.','Resources','cereal.csv')
with open(csvpath, 'rt') as csvfile:
    # Read object to read csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        currentFiber = float(row[7])
        if currentFiber >= 5:
            print(row)
        