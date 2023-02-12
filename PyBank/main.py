# modules
import os
import csv

# set path to to the csv:
budget_csv = os.path.join('Resources', 'budget_data.csv')

# create lists to store read info of total months, profit_loss and profit_loss2
months = []
profit_loss = []
profit_loss2 = []

# open file, specify the variable to hold contents & account for header
with open(budget_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(reader) 

    # loop for info then add months & profit and losses to profit_loss1 & 2 lists
    for row in reader:
        months.append(row[0])
        profit_loss.append(row[1])
        profit_loss2.append(row[1])

# prepare for subtraction using pop and append on profit_loss2 and list comprehension to convert to int for both profit_loss1 & 2
profit_loss2.pop(0)
profit_loss2.append(profit_loss[(len(profit_loss) - 1)])
newprofit_loss = [int(item) for item in profit_loss]
newprofit_loss2 = [int(item) for item in profit_loss2]   

# create list profit_changes to hold all individual monthly changes. Run for loop to subtract newprofit_loss1 &2 and append results to profit_changes
profit_changes = list()
for i in range(len(newprofit_loss)):
     monthly_change = (newprofit_loss2[i] - newprofit_loss[i])
     profit_changes.append(monthly_change)

# print summaries: Header, number of Total Months, Total of profit/loss
print("Financial Analysis")
print("-" * 30)
print("Total Months: " + str(len(months)))
print("Total: $" + str(sum(newprofit_loss)))

# determine and print Average Change
average_change = round(sum(profit_changes)/(len(profit_changes) - 1), 2)
print("Average Change: $" + str(average_change))

# create a function to detrmine max increase and decrease (greatest_amount), their respective indexes (adding + 1 to account for differential) and corresponding months (greatest_month);
def biggest_change(maxormin, incordec):
    greatest_amount = (maxormin(profit_changes))
    greatest_month = months[profit_changes.index(maxormin(profit_changes))+1]
    output = (str(greatest_month) + " ($" + str(greatest_amount) + ")")
    changetype = incordec
    print("Greatest " + str(changetype) + " in Profits: " + output)
    return ("Greatest " + str(changetype) + " in Profits: " + output)

# run function and create variables to hold both desired outputs
grincrease = biggest_change(max, "Increase")
grdecrease = biggest_change(min, "Decrease")
