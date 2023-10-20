import csv

# Initialize a variable
total_votes = 0
candidate_list = {}

# Specify the path to the CSV file to analyze
file_path = "election_data.csv"

# Open and read the data from the CSV file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)

    # Count total votes and votes for each candidate
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidate_list:
            candidate_list[candidate] += 1
        else:
            candidate_list[candidate] = 1

# Print the election results
print("       Election Results")
print("----------------------------------------------------")
print("Total Votes: ", total_votes)
print("----------------------------------------------------")
print("     Candidates:             Percentage:    Votes:  ")
print("----------------------------------------------------")

# Create a string to accumulate the results
results_string = ""

# Calculate and print the results  
for candidate, votes in candidate_list.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate:<30} {percentage:.3f}% {votes:>13}")
    results_string += f"{candidate:<30} {percentage:.3f}% {votes:>13}\n"

print("----------------------------------------------------")

# Determine and print the winner
winner = max(candidate_list, key=candidate_list.get)
print(f"Winner: {winner}")
results_string += ("-----------------------------------------------------\n")
results_string += f"Winner: {winner}\n"
print("-----------------------------------------------------")

# Save the results to a text file
with open("../analysis/candidate_analysis.txt", "w") as outputfile:
    outputfile.write("----------------------------------------------------\n")
    outputfile.write("                   Election Results\n")
    outputfile.write("----------------------------------------------------\n")
    outputfile.write(f"Total Votes: {total_votes}\n")
    outputfile.write("----------------------------------------------------\n")
    outputfile.write("     Candidates:             Percentage:    Votes:\n")
    outputfile.write("----------------------------------------------------\n")
    outputfile.write(results_string)
    outputfile.write("-----------------------------------------------------\n")