import csv
file = "budget_data.csv"


with open (file , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader)
    profits = []    
    date = []
    change_profit = []

    for row in csvreader:
        profits.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:", len(date))
    print("Total Profits:", sum(profits)) 
    for i in range(1 , len(profits)):
        change_profit.append(profits[i] - profits[i-1])
        avg_profit_change = sum(change_profit)/len(change_profit)
        max_profit_change = max(change_profit)
        min_profit_change = min(change_profit)
        max_profit_change_date = str(date[change_profit.index(max(change_profit))])
        min_profit_change_date = str(date[change_profit.index(min(change_profit))])


    print("Avereage Revenue Change: $", round(avg_profit_change))
    print("Greatest Increase in Revenue:", max_profit_change_date,  "($", max_profit_change,")")
    print("Greatest Decrease in Revenue:", min_profit_change_date, "($", min_profit_change,")")



 


