# Required imports

import csv
import os

# path of raw data

raw_results_file = "Resources\\budget_data.csv"

# variables to profit and loss data

tot_months = 0
tot_net = 0
rowbefore_profit = 0
changes = []
dates = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# import data file for analysis

with open(raw_results_file) as raw_bank_data:
    reader = csv.reader(raw_bank_data)
    header = next(reader)

    # process file data

    first_row = next(reader)
    tot_months += 1
    tot_net += int(first_row[1])
    rowbefore_profit = int(first_row[1])

    for row in reader:
        # count months
        tot_months +=1

        # calculate net profit over entire period

        tot_net += int(row[1])

        # calculate change month over month

        row_profit = int(row[1])
        month_change = row_profit - rowbefore_profit
        changes.append(month_change)
        dates.append(row[0])

        # determine greatest increase in profit

        if month_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = month_change

        # determine greatest decrease in profit
        if month_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = month_change

        rowbefore_profit = row_profit

average_profit_change = sum(changes) / len(changes)

print("\nFinancial Analysis")
print("\n-------------------")
print(f"\nTotal Months: {tot_months}")
print(f"\nTotal: ${tot_net:,.2f}")
print(f"\nAverage change: ${average_profit_change:,.2f}")
print(f"\nGreatest increase in profit: {greatest_increase[0]} ${greatest_increase[1]:,.2f}")
print(f"\nGreatest decrease in profit: {greatest_decrease[0]} {greatest_decrease[1]:,.2f}")
print("\n")

# all of above works DO NOT TOUCH

# create and output csv
folder_path = "C:\\Users\\andre\\Rutgers_Codes\\Module_3_Challenge\\python-challenge\\Pybank\\analysis"

file_path = os.path.join(folder_path, "bank_results.csv")
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Total Months", tot_months])
    writer.writerow(["Total", f"${tot_net:,.2f}"])
    writer.writerow(["Average Change", f"${average_profit_change:,.2f}"])
    writer.writerow(["Greatest Increase in Profit", f"{greatest_increase[0]} ${greatest_increase[1]:,.2f}"])
    writer.writerow(["Greatest Decrease in Profit", f"{greatest_decrease[0]} ${greatest_decrease[1]:,.2f}"])
    


