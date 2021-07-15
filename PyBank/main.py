import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
total_months = 0
total = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)

        # Total number of months included in the dataset
        total_months += 1

        # Net total amount of “Profit/Losses” over the entire period
        total += float(row[1])

        # REVISIT - Add calculations for the following:
        # Calculate the changes in “Profit/Losses” over the entire period, then find the average of those changes
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period

    # REVISIT - Write out to analysis.txt instead of printing out
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total:.2f}")

    # REVISIT - Allow user to specify input/output files