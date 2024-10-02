import csv
import os
 
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construct file paths relative to the script location
file_to_load = os.path.join(script_dir, "Resources", "election_data.csv")
file_to_output = os.path.join(script_dir, "analysis", "election_analysis.txt")
 
# Print the file paths for debugging
print(f"Attempting to load file from: {file_to_load}")
print(f"Output will be saved to: {file_to_output}")
 
# Initialize variables
total_votes = 0
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
 
# Process the CSV file
try:
    with open(file_to_load, 'r') as election_data:
        reader = csv.reader(election_data)
        header = next(reader)  # Skip the header row
 
        for row in reader:
            total_votes += 1
            candidate_name = row[2]
 
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
 
    # Prepare and write the output
    output_lines = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_votes}",
        "-------------------------"
    ]
 
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        output_lines.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")
 
        if votes > winning_count:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
 
    output_lines.extend([
        "-------------------------",
        f"Winner: {winning_candidate}",
        f"Winning Vote Count: {winning_count}",
        f"Winning Percentage: {winning_percentage:.3f}%",
        "-------------------------"
    ])
 
    # Print to console
    for line in output_lines:
        print(line)
 
    # Write to file
    os.makedirs(os.path.dirname(file_to_output), exist_ok=True)
    with open(file_to_output, "w") as txt_file:
        txt_file.write("\n".join(output_lines))
 
    print(f"\nResults have been saved to {file_to_output}")
 
except FileNotFoundError:
    print(f"Error: File '{file_to_load}' not found. Please check the file path.")
    print("Make sure the 'Resources' folder with 'election_data.csv' is in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {e}")