# find The average of the changes in "Profit/Losses" over the entire period
# export result to file

import os
import csv
import re

def generateReport(total_months,total,maxProfitDate,maxProfitIncrease,minProfitDate,minProfitDecrease):
    print ("\nFinancial Analysis ")
    print ("---------------------------- ")
    print (f"Total Months: {total_months}")
    print (f"Total: ${total}")
    # find avg
    print (f"Greatest Increase in Profits: {maxProfitDate} (${maxProfitIncrease})")
    print (f"Greatest Decrease in Profits:: {minProfitDate} ($-{minProfitDecrease})")

    output_file_path = os.path.join('.','Resources','result.txt')
    with open(output_file_path, 'w') as resultfile:
        resultfile.write("\nFinancial Analysis\n")
        resultfile.write ("----------------------------\n")
        resultfile.write (f"Total Months: {total_months}\n")
        resultfile.write (f"Total: ${total}\n")
        # find avg
        resultfile.write (f"Greatest Increase in Profits: {maxProfitDate} (${maxProfitIncrease})\n")
        resultfile.write (f"Greatest Decrease in Profits:: {minProfitDate} ($-{minProfitDecrease})\n")
    


def isLess(src, comp): 
    return src < comp

csvpath = os.path.join('.','Resources','budget_data.csv')
with open(csvpath, 'rt') as csvfile:
    total_months = 0
    total = 0

    # Read object to read csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    previousProfitValue = 0
    maxProfitIncrease = 0
    profitChange = 0
    minProfitDecrease = 0
    for row in csvreader:
        currentDate = str(row[0])
        currentProfit = int(row[1])
        total_months = total_months + 1
        total += currentProfit
        profitIncrease = currentProfit-previousProfitValue
        # print(f"profitIncrease {profitIncrease}")
        # print(f"profitChange {profitChange}")
        profitChange += profitIncrease
        profitDecrease = previousProfitValue-currentProfit
        if isLess(maxProfitIncrease,profitIncrease) :
            maxProfitIncrease = profitIncrease
            maxProfitDate = currentDate
        if isLess(minProfitDecrease, profitDecrease):
            minProfitDecrease = profitDecrease 
            minProfitDate = currentDate
        previousProfitValue = currentProfit # set previousProfitValue for next iteration
    # print(f"profitChange : {profitChange}")
    generateReport(total_months,total,maxProfitDate,maxProfitIncrease,minProfitDate,minProfitDecrease)