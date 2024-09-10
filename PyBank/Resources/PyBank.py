import os
import csv

# Specify the path to the CSV file
file_to_load = "PyBank\\Resources\\budget_data.csv"

# Initialize variables for summary statistics
total_months = 0
total_amount = 0
previous_amount = None
changes = []
dates = []  # List to store dates

# Open the CSV file and calculate summary statistics
with open(file_to_load, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        total_months += 1
        total_amount += int(row[1])
        if previous_amount is not None:
            change = int(row[1]) - previous_amount
            changes.append(change)
            dates.append(row[0])  # Store the date for the change
        previous_amount = int(row[1])

# Calculate additional summary statistics
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Get the index of the greatest increase and decrease
greatest_increase_index = changes.index(greatest_increase)
greatest_decrease_index = changes.index(greatest_decrease)

# Get the corresponding dates for the greatest increase and decrease
greatest_increase_date = dates[greatest_increase_index + 1]  # +1 because changes start from the second month
greatest_decrease_date = dates[greatest_decrease_index + 1]  # +1 for the same reason

# Print the summary data in the specified format
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Specify the path to the Resources folder
resources_folder = "C:\\Users\\ayayloyan\\OneDrive - SourceAmerica\\Documents\\GitHub\\Python-Challenge\\PyBank\\Resources"

# Write the summary data to a file in the Resources folder
output_file = os.path.join(resources_folder, "budget_analysis.txt")
with open(output_file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${total_amount}\n")
    output.write(f"Average Change: ${average_change:.2f}\n")
    output.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Summary data has been printed and saved in the 'Resources' folder.")