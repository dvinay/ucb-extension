### Introduction to Python II ###

The following **concepts** has been coverd in this class:
* Feb-25-2019

* [x] Python coding - practice programs
    * [-] print statement
        ```
        print("Hello world")
        ```
    * [-] read input from use
        ```
          age = int(input("Enter your age"))
        ```
    * [-] List in python
        ```
        candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
             "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]
        for candy in candyList:
    		print("[" + str(candyList.index(candy)) + "] " + candy)
        ```
    * [-] How to read csv files
        ```
        # First we'll import the os module
		# This will allow us to create file paths across operating systems
		import os

		# Module for reading CSV files
		import csv

		csvpath = os.path.join('..', 'Resources', 'accounting.csv')

		# Method 1: Plain Reading of CSV files
		with open(csvpath, 'r') as file_handler:
		     lines = file_handler.read()
		     print(lines)
		     print(type(lines))
		```
	* [-] How to read csv files
		```
		# First we'll import the os module
		# This will allow us to create file paths across operating systems
		import os

		# Module for reading CSV files
		import csv

		csvpath = os.path.join('..', 'Resources', 'accounting.csv')
		# Method 2: Improved Reading using CSV module

		with open(csvpath, newline='') as csvfile:

		    # CSV reader specifies delimiter and variable that holds contents
		    csvreader = csv.reader(csvfile, delimiter=',')

		    print(csvreader)

		    # Read the header row first (skip this step if there is now header)
		    csv_header = next(csvreader)
		    print(f"CSV Header: {csv_header}")

		    # Read each row of data after the header
		    for row in csvreader:
		        print(row)
        ```
    * [-] How to write csv files
        ```
        import os
		import csv

		output_path = os.path.join('.','Resources','new.csv')

		with open(output_path, 'w', newline='') as csvfile:
		# with open(csvpath, 'rt') as csvfile:
		    csvWriter = csv.writer(csvfile, delimiter=',')
		    csvWriter.writerow(['First Name','Last Name', 'SSN'])
		    csvWriter.writerow(['apple','orange', '1234'])
        ```
    * [-] How to Zip list data in python
        ```
        import os
		import csv

		indexes = [1,2,3]
		employees = ['Michael','Dwight', 'Merch']
		department = ['Boss','copy', 'data']

		roster = zip(indexes,employees,department)

		for employee in roster:
		    print(employee)
        ```
        output:
        ```
        (1, 'Michael', 'Boss')
		(2, 'Dwight', 'copy')
		(3, 'Merch', 'data')
        ```
    * [-] How to write functions
        ```
		def printHello():
		    print(f"Hello!")
        ```

* [x] Excercise
  * [-] Netflix
  * [-] Udemy
