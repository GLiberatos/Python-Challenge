# Import the CSV module to work with CSV files
import csv

# Initialize variables to store the results
total_months = 0  # To count the total number of months
net_total = 0  # To calculate the net total profit/loss
previous_profit_loss = 0  # To keep track of the previous month's profit/loss
profit_loss_changes = []  # To store the changes in profit/loss
greatest_increase = {"date": "", "amount": 0}  # To track the greatest increase in profit
greatest_decrease = {"date": "", "amount": 0}  # To track the greatest decrease in profit

# Specify the path to the CSV file we want to analyze
file_path = "budget_data.csv"

# Open and read the data from the CSV file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)  # Create a CSV reader object
    
    # Skip the header row
    next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        date = row[0]  # Get the date from the current row
        profit_loss = int(row[1])  # Get the profit/loss value and convert it to an integer
        
        # Calculate the total number of months and net total profit/loss
        total_months += 1
        net_total += profit_loss
        
        # Calculate the change in profit/loss compared to the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            
            # Check if this change is the greatest increase or decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        # Update the previous month's profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print the results to the console
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Save the results to a text file
with open("../analysis/financial_analysis.txt", "w") as outputfile:
    outputfile.write("Financial Analysis\n")
    outputfile.write("------------------\n")
    outputfile.write(f"Total Months: {total_months}\n")
    outputfile.write(f"Total: ${net_total}\n")
    outputfile.write(f"Average Change: ${round(average_change, 2)}\n")
    outputfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    outputfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
