import os
import csv

output_path = os.path.join('.','Resources','new.csv')

with open(output_path, 'w', newline='') as csvfile:
# with open(csvpath, 'rt') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',')
    csvWriter.writerow(['First Name','Last Name', 'SSN'])
    csvWriter.writerow(['apple','orange', '1234'])