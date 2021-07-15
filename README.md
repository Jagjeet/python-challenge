# python-challenge

This challenge analyzes banking and polling data. For more information see the individual sections for PyBank and PyPoll.

## Setup

Clone the respository and follow the usage instructions for PyBank or PyPoll accordingly.

## PyBank

PyBank analyzed CSV data found in `budget_data.csv` containing columns for the `Date` and `Profit/Losses` The script generates the following information:

* The total number of months included in the dataset
* The net total amount of “Profit/Losses” over the entire period
* The changes in “Profit/Losses” over the entire period, then find the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period

### PyBank Usage

The PyBank script can be ran from the PyBank directory using the command `python main.py`. It will output a text file to the analysis directory and to standard output.

### PyBank Known Issues

* Only the first maximum and minimum profit increase and decrease are captured. If a month tied, currently the functionality does not work
* While it was not a requirement, it would be nice to take an input and outfile file as commandline arguments.

## PyPoll

PyPoll analyzed CSV data found in `election_data.csv` containing columns for the `VoterID`, `County` and `Candidate` The script generates the following information:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

### PyPoll Usage

The PyPoll script can be ran from the PyPoll directory using the command `python main.py`. It will output a text file to the analysis directory and to standard output.

### PyPoll Known Issues

* Currently ties are not handled well. The program will simply print a message and exit
* While it was not a requirement, it would be nice to take an input and outfile file as commandline arguments.

## References

The PyBank and PyPoll analyses made use of the following concepts and links:

### Printing Without a New Line

* https://careerkarma.com/blog/python-print-without-new-line/

### File opening for read/write/overwrite

* https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/
* https://www.pythontutorial.net/python-basics/python-read-text-file/
* https://www.pythontutorial.net/python-basics/python-write-text-file/

### Summing values from a dictionary

* https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary

### Fixed Digits

* https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

### Destructuring Assignment

* https://riptutorial.com/python/example/14981/destructuring-assignment
