import csv
from pathlib import Path

# Set the path to the CSV file.
data_folder = Path(__file__).parent.absolute()/Path("Resources/")
file_path = data_folder/"budget_data.csv"

# Initialize variables to store financial analysis results
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
changes_in_profit_losses = []
dates = []

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Extract date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total profit/loss over the entire period
        total_profit_losses += profit_loss

        # Calculate the change in profit/loss from the previous month
        if total_months > 0:
            change = profit_loss - previous_profit_loss
            changes_in_profit_losses.append(change)
            dates.append(date)

        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

        # Count the total number of months
        total_months += 1

# Calculate the average change in profit/loss
average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes_in_profit_losses)
greatest_increase_date = dates[changes_in_profit_losses.index(greatest_increase)]

greatest_decrease = min(changes_in_profit_losses)
greatest_decrease_date = dates[changes_in_profit_losses.index(greatest_decrease)]

# Print the financial analysis results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


# Export the results to a text file
output_file_path = data_folder/"financial_analysis_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Results saved to:", output_file_path)