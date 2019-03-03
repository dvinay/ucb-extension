# PyPoll Solution

import os
import math
import csv
import re

# generate the report content
def generateReportContent(total_votes, candidates, candidates_count):
    precision = 3
    result = ""
    for i in range(len(candidates)):
        percentage = int(candidates_count[i])/int(total_votes)*100
        result = result + f"{candidates[i]}: {'{:.{}f}'.format( percentage, precision )}% ({candidates_count[i]})\n"
    
    data = "\nElection Results \n" + "-------------------------\n" + f"Total Votes: {total_votes}\n" + "-------------------------\n" + result + "-------------------------\n" + f"Winner: {candidates[candidates_count.index(max(candidates_count))]}\n" + "-------------------------\n"
    return data

# display the report to terminal
def displayReport(data):
    print (data)

# write Report to File
def writeReportFile(data):
    output_file_path = os.path.join('.','Resources','result.txt')
    with open(output_file_path, 'w') as resultfile:
        resultfile.write (data)
        resultfile.close()

# Read the input file
csvpath = os.path.join('.','Resources','election_data.csv')
with open(csvpath, 'rt') as csvfile:
    # The total number of votes cast
    total_votes = 0
    candidates = ["Khan","Correy","Li","O'Tooley"]
    candidates_count = [0,0,0,0]

    # Read object to read csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # A complete list of candidates who received votes
    for row in csvreader:
        total_votes = total_votes + 1
        if(row[2] == candidates[0]):
            candidates_count[0] = candidates_count[0]+1
        elif(row[2] == candidates[1]):
            candidates_count[1] = candidates_count[1]+1
        elif(row[2] == candidates[2]):
            candidates_count[2] = candidates_count[2]+1
        elif(row[2] == candidates[3]):
            candidates_count[3] = candidates_count[3]+1
        else:
            print("candidate not found ${row[2]}")

    # prepare the report result content
    result = generateReportContent(total_votes, candidates, candidates_count)
    
    # display the report to terminal
    displayReport(result)

    # write Report to File
    writeReportFile(result)