import csv
import os

# Specify the path to the CSV file
file_to_load = "C:\\Users\\ayayloyan\\OneDrive - SourceAmerica\\Documents\\GitHub\\Python-Challenge\\PyPoll\\Resources\\election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_to_load) as poll_data:
    reader = csv.reader(poll_data)
    # Skip the header
    next(reader)

    # Count total votes and votes for each candidate
    for row in reader:
        if len(row) < 3:
            continue  # Skip rows that do not have enough elements
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate percentages and find the winner
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes, percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify the path to the Resources folder
resources_folder = "C:\\Users\\ayayloyan\\OneDrive - SourceAmerica\\Documents\\GitHub\\Python-Challenge\\PyPoll\\Resources"

# Write the summary data to a file in the Resources folder
output_file = os.path.join(resources_folder, "PyPoll.txt")
with open(output_file, 'w') as output:
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-------------------------\n")
    for candidate, votes, percentage in results:
        output.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("-------------------------\n")

print("Summary data has been printed and saved in the 'Resources' folder.")