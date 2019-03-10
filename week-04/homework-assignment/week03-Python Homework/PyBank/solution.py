import os
import csv
import re

def generateReportContent(total_months,total,average_change,maxProfitDate,maxProfitIncrease,minProfitDate,minProfitDecrease):
    # display precision part after decimal value
    precision = 2
    average_change_result = f"{'{:.{}f}'.format( average_change, precision )}"
    data = "\nFinancial Analysis \n" + "---------------------------- \n" + f"Total Months: {total_months}\n" + f"Total: ${total}\n" + f"Average  Change: ${average_change_result}\n"+f"Greatest Increase in Profits: {maxProfitDate} (${maxProfitIncrease})\n" + f"Greatest Decrease in Profits:: {minProfitDate} ($-{minProfitDecrease})\n"
    return data

# display the report to terminal
def displayReport(data):
    print (data)

# write Report to File
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
    average_change = 0
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
        

        profitIncrease = currentProfit-previousProfitValue
        profitDecrease = previousProfitValue-currentProfit
        if maxProfitIncrease < profitIncrease :
            maxProfitIncrease = profitIncrease
            maxProfitDate = currentDate
        if minProfitDecrease < profitDecrease:
            minProfitDecrease = profitDecrease 
            minProfitDate = currentDate
        # set previousProfitValue for next iteration    
        previousProfitValue = currentProfit 
        if(total != 0 ): #don't calculate profitChange for first row
            profitChange = profitChange+profitIncrease
        total += currentProfit
    # print(f"Final profitChange  : {profitChange}")
    average_change = profitChange / (total_months-1)
    # prepare the report result content
    result = generateReportContent(total_months,total,average_change,maxProfitDate,maxProfitIncrease,minProfitDate,minProfitDecrease)
    
    # display the report to terminal
    displayReport(result)

    # write Report to File
    writeReportFile(result)
    