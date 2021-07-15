import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
total_months = 0
total = 0
count = 0
prev_profit_loss = 0
profit_loss_changes = []
average_change = 0
average_profit_loss = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for index, row in enumerate(csvreader):
        # print(row)
        date = row[0]
        profit_loss = float(row[1])

        # Total number of months included in the dataset
        total_months += 1

        # Net total amount of “Profit/Losses” over the entire period
        total += profit_loss

        # Calculate the changes in “Profit/Losses” over the entire period
        if (index != 0):
          profit_loss_changes.append(profit_loss - prev_profit_loss)
          prev_profit_loss = profit_loss
          count = index
        else:
          prev_profit_loss = profit_loss


        # REVISIT - Add calculations for the following:
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period

    #Calculate average of the profit/loss changes
    average_profit_loss = sum(profit_loss_changes)/count

    # REVISIT - Write out to analysis.txt instead of printing out
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total:.2f}")
    print(f"Average Change: {average_profit_loss:.2f}")

    # REVISIT - Allow user to specify input/output files