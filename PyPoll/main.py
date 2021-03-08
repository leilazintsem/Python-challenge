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
total_rows=0
total_candidates = 0

#create a file path 
csvpath = os.path.join ('Resources', 'sample_data.csv')

 # open the file
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#calculate the total number of votes assuming every voter votes once

    for rows in csvreader:
        total_rows = total_rows + 1
    print("Total Votes : " , total_rows)
    
# list of candidates who received votes
#find uniques values
    candidates.append(rows[3])
    print(candidates)
