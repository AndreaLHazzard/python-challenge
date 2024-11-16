# Required imports

import csv
import os

# path of raw data

raw_results_file = "Resources\\election_data.csv"

# variables to hold candidate and count information

vote_count = 0
candidates = {}
winner = ""
votes_to_win = 0

# import the results file for analysis

with open(raw_results_file) as raw_data:
    reader = csv.reader(raw_data)
    header = next(reader)

    # begin reading and summariZing the raw data

    for row in reader:
        vote_count +=1
        candidate_name = row[2]

        # add candidates to candidates dictionary and count votes

        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] +=1
        
        # determine percentage of vote
        
for candidate, votes in candidates.items():
    percentage_vote = float(votes) / float(vote_count) * 100  

    if votes > votes_to_win:
        votes_to_win = votes
        winner = candidate

# print total results and individual results 
# Chatgpt for formatting percentage_vote as %

print("\nTotal Votes: " + str(vote_count))
print("\n------------------------")
for candidate, votes in candidates.items():
    percentage_vote = float(votes) / float(vote_count) * 100  
   
    print(f"\n{candidate}: {percentage_vote:.3f}% ({votes})")
    
# determine and print the winner

print("\n------------------------")
print("\nWinner: " + winner)
print("\n------------------------")
 
 # all of the above works DO NOT TOUCH

# output to csv

folder_path = "analysis"
os.makedirs(folder_path, exist_ok=True)


file_path = os.path.join(folder_path, "election_results.csv")
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header
   # writer.writerow(["Description", "Details"])
    
    # Write total votes
    writer.writerow(["Total Votes", vote_count])
    writer.writerow([])
    
    # Write candidate results
    writer.writerow(["Candidate", "Percentage", "Votes"])
    for candidate, votes in candidates.items():
        percentage_vote = float(votes) / float(vote_count) * 100
        writer.writerow([candidate, f"{percentage_vote:.3f}%", votes])
    writer.writerow([])
    
    # Write the winner
    writer.writerow(["Winner", winner])
