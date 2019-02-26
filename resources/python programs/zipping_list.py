import os
import csv

indexes = [1,2,3]
employees = ['Michael','Dwight', 'Merch']
department = ['Boss','copy', 'data']

roster = zip(indexes,employees,department)

for employee in roster:
    print(employee)