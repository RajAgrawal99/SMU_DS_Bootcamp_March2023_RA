# begin from here-------i have taken help code from our instructor
#
import  csv

# my file path ------
csv_path = "PyBank/Resources/budget_data.csv"

# for each row
# add 1 to some month counter
# add column 2 (B) to some profit counter

months = 0
total_profit = 0

is_first_row = True
last_month_profit = 0
changes = []

# max change
# max month
max_change = -99999999999
max_month = ""

# min change
# min month
min_change = 999999999999999999
min_month = ""

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        row_profit = int(row[1])

        # check if first row (no change in first month but need to init last_month_profit)
        if is_first_row:
            last_month_profit = row_profit
            is_first_row = False
        else:
            change = row_profit - last_month_profit
            changes.append(change)

            # reset for the next month
            last_month_profit = row_profit

            # compared to max/min
            if change > max_change:
                 max_change = change
                 max_month = row[0]

            if change < min_change:
                min_change = change
                min_month = row[0]

        months += 1
        total_profit += int(row[1])

# ouput to terminal
    print("********************************")

    print(months)
    print(total_profit)

    avg_changes = sum(changes) / len(changes)
    print(avg_changes)

    print(max_month, max_change)
    print(min_month, min_change)

# ouput to a file
f = open("PyBank/analysis/PyBankResult.txt", "w")
print("Total Months : ", months, file=f),
print("Total Profit : ", total_profit, file=f),
print("Average Changes : ", avg_changes,file=f),
print("Greatest Increase in Profits : ", max_month, max_change, file=f),
print("Greatest Decrease in Profits : ", min_month, min_change, file=f)
# last line ----only for reference