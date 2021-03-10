# ## Pseudocode:
# i am being asked to help a rural town modernize it s vote counting
#     I have a data set composed of three columns: `Voter ID`, `County`, and `Candidate`
#         Your task is to create a Python script that analyzes the votes and calculates each of the following
#             * The total number of votes cast
#             * A complete list of candidates who received votes
#             * The percentage of votes each candidate won
#             * The total number of votes each candidate won
#             * The winner of the election based on popular vote
#             specific output
#             Election Results
#             -------------------------
#             Total Votes: 3521001
#             -------------------------
#             Khan: 63.000% (2218231)
#             Correy: 20.000% (704200)
#             Li: 14.000% (492940)
#             O'Tooley: 3.000% (105630)
#             -------------------------
#             Winner: Khan
#             -------------------------

#Lets Import our modules
import os 
import csv

#Declare your variables
voter_id = []
county = []
candidates = []
total_votes=0
total_candidates = 0
a_candidate = 0
candidates_dict ={}
winner=""
max_vote = 0
#create a file path 
csvpath = os.path.join ('Resources', 'election_data.csv')

 # open the file
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    print("Election Results")
    print("-------------------------")
#calculate the total number of votes assuming every voter votes once

    for rows in csvreader:
        total_votes = total_votes + 1
        voter_id.append(rows[0])
        county.append(rows[1])
        if rows[2] not in candidates:
            candidates.append(rows[2])
            candidates_dict[rows[2]] = 0
        candidates_dict[rows[2]] = candidates_dict[rows[2]] +1

    print(f"Total Votes :  {total_votes}")
    print("-------------------------------")

    #print(candidates)
    for i in candidates_dict:
        C_votes = candidates_dict[i] 
        percentage = 100*(C_votes/total_votes)
        percentage = "%.3f" % percentage
        print(f'{i}: {percentage} %, ({C_votes})')
        if C_votes > max_vote:
            max_vote = C_votes
            winner = i 
    print("-----------------------------------")
    print(f'winner: {winner}')
    print("-----------------------------------")


#Specify the file to write to
output_file = os.path.join("Analysis","output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("----------------------------------------\n")
    textfile.write(f"Total Votes :  {total_votes}\n")
    textfile.write("-------------------------------\n")
    textfile.write(f"{i}: {percentage} %, ({C_votes})\n")
    textfile.write("-----------------------------------\n")
    textfile.write(f"winner: {winner}\n")
    textfile.write("-----------------------------------\n")