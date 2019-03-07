
# import modules
import os
import csv

# path to file
csvpath = os.path.join('Resources', 'budget_data.csv')

# create variable lists
total_months = []
total_profit = []

# open file, and read it
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader) #skip first line for iteration, call it header
    
    # iterate through the file, line by line, populating lists with values from column1 and 2
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(row[1])

    # The total number of months included in the dataset is same as length of the column1
    total_number_of_months = len(total_months)
    
    # The net total amount of "Profit/Losses" over the entire period
    total_profit = list(map(int, total_profit)) # convert to from list of stings to list of ints
    net_total = sum(total_profit)
    
    # The average of the changes in "Profit/Losses" over the entire period
    average_change = net_total / total_number_of_months

    # The greatest increase in profits (date and amount) over the entire period
    greatest_increase_amount = max(total_profit) # find max in the list
    total_increase_index = total_profit.index(greatest_increase_amount) # find number of that index in profit
    greatest_increase_date = total_months[total_increase_index] # find value for the same index in months column
    
    # The greatest decrease in losses (date and amount) over the entire period
    greatest_loss_amount = min(total_profit)
    total_loss_index = total_profit.index(greatest_loss_amount)
    greatest_loss_date = total_months[total_loss_index]


#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)

print_file = (f"  Financial Analysis \n"
      f"  ----------------------------\n"
      f"  Total Months: {total_number_of_months}\n"
      f"  Total: ${net_total}\n"
      f"  Average  Change: ${'{:.2f}'.format(average_change)}\n"
      f"  Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n"
      f"  Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss_amount})\n")

print(print_file)

# create output file for the analysis report
output_file = os.path.join("Financial_Analysis.txt")

with open('Financial_Analysis.txt', 'w') as the_file:
    the_file.write(print_file)

