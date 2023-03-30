

import os

import csv

cvspath= os.path.join('..', 'Resources', 'budget_data.csv')
print(cvspath)

budget_data = []

with open(cvspath, 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')


    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]), "change": 0})


Total_months = len(budget_data)

Previous_amount = budget_data [0] ["amount"]
for i in range (Total_months):
    budget_data [i] ["change"] = budget_data [i] ["amount"] - Previous_amount
    Previous_amount = budget_data [i] ["amount"]


total_amount = sum(row['amount'] for row in budget_data)

total_change = sum(row['change'] for row in budget_data)
average = round(total_change / (Total_months-1), 2)


get_increase = max(budget_data, key= lambda x:x['change'])
get_decrease = min(budget_data, key=lambda x:x['change'])

print('Financial Analysis')
print('--------------------------------')
print(f'Total Months: {Total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Great Increase in profit: {get_increase["month"]}  (${get_increase["change"]})')
print(f'Greatest Decrease in profits: {get_decrease["month"]} (${get_decrease["change"]})')


filepath = os.path.join('.', 'Resource', 'Pybank_results.txt')
with open(filepath, "w") as text_file:
     print('Financial analysis', file=text_file)
     print('------------------------------------', file=text_file)
     print(f'Total month: {Total_months}', file=text_file)
     print(f'Total: ${total_amount}', file=text_file)
     print(f'Average Change: ${average}', file=text_file)
     print(f'Greatest Increase in profits: {get_increase["month"]} (${get_increase["change"]})',file=text_file)
     print(f'Greatest Decrease in profit: {get_decrease["month"]} (${get_decrease["change"]})', file=text_file)
