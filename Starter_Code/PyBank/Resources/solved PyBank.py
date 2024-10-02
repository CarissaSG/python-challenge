import csv
import os
 
# Ensure correct file path based on your file location
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "financial_analysis.txt")
 
# Define variables to track the financial data
total_months = 0
total_net = 0
previous_value = None
net_changes = []
months = []
greatest_increase = {"month": "", "amount": float('-inf')}
greatest_decrease = {"month": "", "amount": float('inf')}
 
# Error handling using try-except block for FileNotFoundError
try:
    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)
 
        # Skip the header row
        header = next(reader)
 
        # Process each row of data
        for row in reader:
            # Track the total months and total net amount
            total_months += 1
            value = int(row[1])
            total_net += value
 
            # Calculate net change (skip for the first row)
            if previous_value is not None:
                net_change = value - previous_value
                net_changes.append(net_change)
                months.append(row[0])
 
                # Update greatest increase and decrease
                if net_change > greatest_increase['amount']:
                    greatest_increase['month'] = row[0]
                    greatest_increase['amount'] = net_change
                if net_change < greatest_decrease['amount']:
                    greatest_decrease['month'] = row[0]
                    greatest_decrease['amount'] = net_change
 
            previous_value = value
 
    # Calculate the average net change
    average_net_change = sum(net_changes) / len(net_changes) if net_changes else 0
 
    # Generate the output summary
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_net_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
        f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})"
    )
 
    # Print the output
    print(output)
 
    # Write the results to a text file
    os.makedirs(os.path.dirname(file_to_output), exist_ok=True)
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
 
except FileNotFoundError:
    print(f"Error: File '{file_to_load}' not found. Please check the file path.")