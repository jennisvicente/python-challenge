# Module for reading CSV files

import csv

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
# CSV reader specifies delimiter and variable that holds contents
file = "budget_data.csv"
#Lists   
profit = []
monthly_changes = []
date = []
#Variables
all_months = 0
net_profits = 0
change_profit = 0
initial_profit = 0

# Read each row of data after the header
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#The total number of months included in the dataset
    for row in csvreader:
        all_months = all_months + 1
        date.append(row[0])
#The net total amount of "Profit/Losses" over the entire period
        profit.append(row([1])
        net_profits = net_profits + int(row[1])
        

#The average of the changes in "Profit/Losses" over the entire period
        final_profit = int(row[1])
        monthly_profit_change = final_profit - initial_profit
        monthly_changes.append(monthly_profit_change)
        total_profit_change = total_profit_change + monthly_profit_change
        initial_profit = final_profit
        average_profit_change = (total_profit_change/count)

#The greatest increase in profits (date and amount) over the entire period
        greatest_profit_increase = max(monthly_changes)
        date_increase = date[monthly_changes.index(greatest_profit_increase)]

#The greatest decrease in losses (date and amount) over the entire period
        greatest_profit_decrease = min(monthly_changes)
        date_deacrease = date[monthly_changes.index(greatest_profit_decrease)]

#Print analysis
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(all_months))
print("Total Profits: " + "$" + str(net_profits))
print("Average Change: " + "$" + str(int(average_profit_change)))
print("Greatest Increase in Profits: " + str(date_increase) + " ($" + str(greatest_profit_increase) + ")")
print("Greatest Decrease in Profits: " + str(date_decrease) + " ($" + str(greatest_profit_increase)+ ")")
print("----------------------------------------------------------")
