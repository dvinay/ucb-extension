import os
import csv

# Path to collect data from the Resources folder
wrestlingCSV = os.path.join('.','Resources','WWE-Data-2016.csv')
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def getPercentages(wrestlerData):
# Find the total number of matches wrestled
    total_matches = int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3])
# Find the percentage of matches won
    win_matches = int(wrestlerData[1]) / total_matches * 100
# Find the percentage of matches lost
    lost_matches = int(wrestlerData[2]) / total_matches * 100
# Find the percentage of matches drawn
    draw_matches = int(wrestlerData[3]) / total_matches * 100
# Print out the wrestler's name and their percentage stats
    print(f"Stats for {wrestlerData[0]}")
    print(f"WIN PERCENT : {win_matches}")
    print(f"LOSS PERCENT : {lost_matches}")
    print(f"DRAW PERCENT : {draw_matches}")
    print(f"{wrestlerData[0]} is a Superstar")
    
# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)