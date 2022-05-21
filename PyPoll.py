import csv
import os
# The data we need to retrieve
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0


# open the election results and read the file
    # election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:



# Using the with statement open the files as a txt file
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    # txt_file.write("Counties in the Election\n----------------\n")

    # Write thres counties to the file
    # txt_file.write("Arapahoe\nDenver\nJefferson")
    # txt_file.write("Denver\n")
    # txt_file.write("Jefferson")

# Read the file object with the reader function

    file_reader =csv.reader(election_data)

    headers = next(file_reader)

    # print(headers)

# print each row in the csv file

    for row in file_reader:

        # Add to the total vote count    
        total_votes +=1

        # print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates    
            candidate_options.append(candidate_name)

            # Begin tracking candidate votes count
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    # Save the result to txt file
    with open(file_to_save, "w") as txt_file:

        # print the final vote count to the terminal
        election_result = (
            f"\nElection Result\n"
            f"-----------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------\n"
        )
        print(election_result, end="")

        # Save the final vote count to the txt file
        txt_file.write(election_result)

    # Determin the percentage of votes for each candidate by looping through the count
    # 1. Iterate through the candidate list

        for candidate_name in candidate_votes:

            # 2. Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]

            # 3. Calculate the percentage of votes

            vote_percentage = float(votes) / float(total_votes) * 100
            
            # Determin winning vote count and candidate
            # Determin if the votes is greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                # Determine the winnng candiate
                winning_candidate = candidate_name
            # 4. print the candidate name and percentage of votes

            candidate_result = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_result)
            txt_file.write(candidate_result)
    # winning candidate summary
        winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------------------\n"
        )
        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)
# print the candidate votes dictionary
# print(candidate_votes)

# # print the candidate list
# print(candidate_options)

# # print the total number of votes
# print(total_votes)



# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidates won
# 4. The total number of votes each candidates won
# 5. The winner of the election based on popular vote


# election_data.close()