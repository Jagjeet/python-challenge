import os
import csv

SEPARATOR = '-------------------------\n'

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
analysis_path = os.path.join('.', 'analysis', 'analysis.txt')
total_votes = 0

#key = candidate name
#value = number of votes
candidate_dict = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for index, row in enumerate(csvreader):
        voter_id, county, candidate = row

        #The total number of votes cast
        total_votes += 1

        if candidate not in candidate_dict.keys():
            candidate_dict[candidate] = 1

    #REVISIT - calculate the following
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.

    # Write out to analysis.txt
    with open(analysis_path, 'w+') as f:
      f.write('Election Results\n')
      f.write(SEPARATOR)
      f.write(f"Total Votes: {total_votes}\n")
      f.write(SEPARATOR)
      #REVISIT - Add actual calculations and output here
      for candidate in candidate_dict:
          f.write(f"{candidate}: \n")
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