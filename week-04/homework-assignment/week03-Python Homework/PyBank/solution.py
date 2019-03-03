# find The average of the changes in "Profit/Losses" over the entire period
# export result to file

import os
import csv
import re

def generateReportContent(total_months,total,maxProfitDate,maxProfitIncrease,minProfitDate,minProfitDecrease):
    # find avg
    data = "\nFinancial Analysis \n" + "---------------------------- \n" + f"Total Months: {total_months}\n" + f"Total: ${total}\n" + f"Greatest Increase in Profits: {maxProfitDate} (${maxProfitIncrease})\n" + f"Greatest Decrease in Profits:: {minProfitDate} ($-{minProfitDecrease})\n"
    return data

def displayReport(data):
    print (data)

def writeReportFile(data):
    output_file_path = os.path.join('.','Resources','result.txt')
    with open(output_file_path, 'w') as resultfile:
        resultfile.write(data)
        resultfile.close()

# Read the input file
csvpath = os.path.join('.','Resources','budget_data.csv')
with open(csvpath, 'rt') as csvfile:
    total_months = 0
    total = 0
    previousProfitValue = 0
    maxProfitIncrease = 0
    profitChange = 0
    minProfitDecrease = 0
    
    # Read object to read csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        currentDate = str(row[0])
        currentProfit = int(row[1])
        total_months = total_months + 1
        total += currentProfit
        profitIncrease = currentProfit-previousProfitValue
        #print(f"profitIncrease {profitIncrease}")
        
        profitDecrease = previousProfitValue-currentProfit
        if maxProfitIncrease < profitIncrease :
            maxProfitIncrease = profitIncrease
            maxProfitDate = currentDate
        if minProfitDecrease < profitDecrease:
            minProfitDecrease = profitDecrease 
            minProfitDate = currentDate
        # set previousProfitValue for next iteration    
        previousProfitValue = currentProfit 
    # print(f"profitChange : {profitChange}")

    # prepare the report result content
    result = generateReportContent(total_months,total,maxProfitDate,maxProfitIncrease,minProfitDate,minProfitDecrease)
    
    # display the report to terminal
    displayReport(result)

    # write Report to File
    writeReportFile(result)
    