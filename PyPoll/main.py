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

        if candidate in candidate_dict.keys():
            #The total number of votes each candidate won
            candidate_dict[candidate] += 1
        else:
            #A complete list of candidates who received votes
            candidate_dict[candidate] = 1

    # Write out to analysis.txt
    with open(analysis_path, 'w+') as f:
        winner = None
        f.write('Election Results\n')
        f.write(SEPARATOR)
        f.write(f"Total Votes: {total_votes}\n")
        f.write(SEPARATOR)

        #Write out for each candidate
        for candidate in candidate_dict:
            #The percentage of votes each candidate won
            percentage_votes = (candidate_dict[candidate]* 100)/total_votes
            f.write(f"{candidate}: {percentage_votes:.3f}% ({candidate_dict[candidate]})\n")

            #Calculate winner of the election based on popular vote.
            if winner == None or candidate_dict[candidate] > candidate_dict[winner]:
                winner =  candidate
            #Print an error and exit if we have a tie
            #REVISIT - Ties could throw an error or be better handled
            elif candidate_dict[candidate] == candidate_dict[winner]:
                print('Ties are currently unhandled by the script')
                exit(1)
        f.write(SEPARATOR)
        f.write(f"Winner: {winner}\n")
        f.write(SEPARATOR)

    #print out analysis
    with open(analysis_path) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')