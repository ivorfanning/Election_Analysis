import csv
import os
# The data we need to retrieve
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

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

    print(headers)

# print each row in the csv file

    # for row in file_reader:
    #     print(row)



# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidates won
# 4. The total number of votes each candidates won
# 5. The winner of the election based on popular vote


# election_data.close()