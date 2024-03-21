# First I'll import os
# This will allow me to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Although I orgnized my files apropriately, I will still prefer to set path for the file using the os.path.join function
Path_for_budget_data = os.path.join('Resources', 'budget_data.csv')

# Setting the result file path for budget_data analysis
output_file_path = "Budget_Analysis.txt"

# Set variables to store data
Total_Months = []
Total_Profit_Losses = []
Profit_Losses_Change = []
Average_Profit_Change = []
Greatest_Increase_in_Profits = []
Greatest_decrease_in_Profits = []

# MeTo read my csv I will use method 2: Improved Reading using csv 
with open(Path_for_budget_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        Total_Months.append(row[0])
        Total_Profit_Losses.append(int(row[1]))

# Calculate the changes in "profit/losses"
for i in range(len(Total_Profit_Losses) - 1):
    Profit_Losses_Change.append(Total_Profit_Losses[i+1] - Total_Profit_Losses[i])

# Obtain the total number of months
Sum_Months = len(Total_Months)

# Obtain the total "profit/losses"
Sum_Total_Profit_Losses = sum(Total_Profit_Losses)

# Calculate average profit change
Average_Profit_Change = (sum(Profit_Losses_Change) / len(Profit_Losses_Change))

# Calculate the greatest increase and decrease in profits
Greatest_Increase_in_Profits = max(Profit_Losses_Change)
Greatest_decrease_in_Profits = min(Profit_Losses_Change)

# Obtaining corresponding months for greatest increase and decrease in profits
Month_Greatest_Increase_in_Profits = Total_Months[Profit_Losses_Change.index(Greatest_Increase_in_Profits) + 1]
Month_Greatest_decrease_in_Profits = Total_Months[Profit_Losses_Change.index(Greatest_decrease_in_Profits) +1]

# Now printing my results
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {Sum_Months}")
print(f"Total: ${Sum_Total_Profit_Losses:}")
print(f"Avrage Change: ${Average_Profit_Change: .2f}")
print(f"Greatest Increase in Profits: {Month_Greatest_Increase_in_Profits} (${Greatest_Increase_in_Profits})")
print(f"Greatest Decrease in Profits: {Month_Greatest_decrease_in_Profits} (${Greatest_decrease_in_Profits})")

#Transfer these results to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------------------\n")
    output_file.write(f"Total Months: {Sum_Months}\n")
    output_file.write(f"Total: ${Sum_Total_Profit_Losses}\n")
    output_file.write(f"Avrage Change: ${Average_Profit_Change: .2f}\n")
    output_file.write(f"Greatest Increase in Profits: {Month_Greatest_Increase_in_Profits} (${Greatest_Increase_in_Profits})\n")
    output_file.write(f"Greatest Decrease in Profits: {Month_Greatest_decrease_in_Profits} (${Greatest_decrease_in_Profits})\n")
    
