import csv
from pathlib import Path

# Set the path to the CSV file.
data_folder = Path(__file__).parent.absolute()/Path("Resources/")
file_path = data_folder/"election_data.csv"

# Initialize variables to store election analysis results
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Extract candidate name
        candidate = row[2]

        # Count the total number of votes
        total_votes += 1

        # Update candidate vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print the election analysis results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Iterate through candidates to calculate and print their percentage of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Update the winner based on popular vote
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Export the results to a text file
output_file_path = data_folder/"election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Iterate through candidates to calculate and write their percentage of votes
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-------------------------\n")

print("Results saved to:", output_file_path)
