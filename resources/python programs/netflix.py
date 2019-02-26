import os
import csv

movie = input("what video they are looking for")
csvpath = os.path.join('.','Resources','netflix_ratings.csv')
#./Resources
with open(csvpath, newline='') as csvfile:
# with open(csvpath, 'rt') as csvfile:
    readerLine = csv.reader(csvfile, delimiter=',')
    for row in readerLine:
        if row[0] == movie:
            print (f"{movie} is rated {row[1]} with a rating of {row[6]}")
