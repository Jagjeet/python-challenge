import os
import csv

SEPARATOR = '-------------------------\n'

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
analysis_path = os.path.join('.', 'analysis', 'analysis.txt')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # for index, row in enumerate(csvreader):
    #     print(row)

    # Write out to analysis.txt
    with open(analysis_path, 'w+') as f:
      f.write('Election Results\n')
      f.write(SEPARATOR)
      #REVISIT - Add total votes
      f.write(f"Total Votes: \n")
      f.write(SEPARATOR)
      #REVISIT - Add actual calculations and output here
      #Khan: 63.000% (2218231)
      #Correy: 20.000% (704200)
      #Li: 14.000% (492940)
      #O'Tooley: 3.000% (105630)
      f.write(SEPARATOR)
      #REVISIT - Add actual calculations and output here
      #Winner: Khan
      f.write(SEPARATOR)

      #print out analysis
    with open(analysis_path) as f:
      lines = f.readlines()
      for line in lines:
        print(line, end='')