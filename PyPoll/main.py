# First I'll import os
# This will allow me to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Although I orgnized my files apropriately, I will still prefer to set path for the file using the os.path.join function
Path_for_election_data = os.path.join('Resources', 'election_data.csv')

# Setting the result file path for budget_data analysis
output_file_path = "election_Analysis.txt"

# Set variables to store data
Votes = []
candidates = []
Diana_DeGette = []
Charles_Casper_Stockham = []
Raymon_Anthony_Doane = []
Diana_DeGette_Votes = 0
Charles_Casper_Stockham_Votes = 0
Raymon_Anthony_Doane_Votes = 0

# To read my csv I will use method 2: Improved Reading using csv 
with open(Path_for_election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        Votes.append(int(row[0]))
        candidates.append(row[2])

# Count Votes
Total_Votes_Cast = (len(Votes))

# Votes by Individual
for candidates in candidates:
    if candidates == "Diana DeGette":
        Diana_DeGette.append(candidates)
        Diana_DeGette_Votes = len(Diana_DeGette)

    elif candidates == "Charles Casper Stockham":
        Charles_Casper_Stockham.append(candidates)
        Charles_Casper_Stockham_Votes = len(Charles_Casper_Stockham)

    else:
        Raymon_Anthony_Doane.append(candidates)
        Raymon_Anthony_Doane_Votes = len (Raymon_Anthony_Doane)

# Percent votes per candidate
Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_Votes / Total_Votes_Cast) * 100),3)
Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_Votes / Total_Votes_Cast) * 100),3)
Diana_DeGette_percent = round(((Diana_DeGette_Votes / Total_Votes_Cast) * 100),3)

# Who is the winner
if Raymon_Anthony_Doane_percent > max(Charles_Casper_Stockham_percent, Diana_DeGette_percent):
    Winner = "Raymon Anthony Doane"

elif Charles_Casper_Stockham_percent > max(Raymon_Anthony_Doane_percent, Diana_DeGette_percent):
    Winner = "Charles Casper Stockhan"

else:
    Winner = "Diana DeGette"


# Print the results
print("Election Results")

print("-------------------------------")

print(f"Total Votes: {Total_Votes_Cast}")

print("-------------------------------")
print(f"Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_Votes})")

print(f"Diana_DeGette_percent: {Diana_DeGette_percent}% ({Diana_DeGette_Votes})")

print(f"Raymon_Anthony_Doane_percent: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_Votes})")

print("-------------------------------")

print(f"Winner: {Winner}")

print("-------------------------------")

#Transfer results to text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("------------------------------\n")
    output_file.write(f"Total Votes: {Total_Votes_Cast}\n")
    output_file.write("------------------------------\n")
    output_file.write(f"Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_Votes})\n")
    output_file.write(f"Diana_DeGette_percent: {Diana_DeGette_percent}% ({Diana_DeGette_Votes})\n")
    output_file.write(f"Raymon_Anthony_Doane_percent: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_Votes})\n")
    output_file.write("------------------------------\n")
    output_file.write(f"Winner: {Winner}\n")
    output_file.write("------------------------------")