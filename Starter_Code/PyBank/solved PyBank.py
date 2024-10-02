import csv
import os
 
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construct file paths relative to the script location
file_to_load = os.path.join(script_dir, "Resources", "budget_data.csv")
file_to_output = os.path.join(script_dir, "analysis", "financial_analysis.txt")
 
# Print the file paths for debugging
print(f"Attempting to load file from: {file_to_load}")
print(f"Output will be saved to: {file_to_output}")
 
# Rest of your code remains the same
total_months = 0
total_net = 0
previous_value = None
net_changes = []
months = []
greatest_increase = {"month": "", "amount": float('-inf')}
greatest_decrease = {"month": "", "amount": float('inf')}
 
try:
    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)
 
        header = next(reader)
 
        for row in reader:
            total_months += 1
            value = int(row[1])
            total_net += value
 
            if previous_value is not None:
                net_change = value - previous_value
                net_changes.append(net_change)
                months.append(row[0])
 
                if net_change > greatest_increase['amount']:
                    greatest_increase['month'] = row[0]
                    greatest_increase['amount'] = net_change
                if net_change < greatest_decrease['amount']:
                    greatest_decrease['month'] = row[0]
                    greatest_decrease['amount'] = net_change
 
            previous_value = value
 
    average_net_change = sum(net_changes) / len(net_changes) if net_changes else 0
 
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_net_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
        f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})"
    )
 
    print(output)
 
    os.makedirs(os.path.dirname(file_to_output), exist_ok=True)
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
 
except FileNotFoundError:
    print(f"Error: File '{file_to_load}' not found. Please check the file path.")
    print("Make sure the 'Resources' folder with 'budget_data.csv' is in the same directory as this script.")