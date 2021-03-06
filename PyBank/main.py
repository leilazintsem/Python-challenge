#Pseudocode for PyBank Question
# we have some data which are store somwhere
# data store in a cvs file
#we are being asked to create script/manipulate the data contained in csv file 
# to come up with specific script
    # to achieve that, I need to do some math
        # the specific output should look like the following

#        # Financial Analysis
# ----------------------------
#         Total Months: 86
#         Total: $38382578
#         Average  Change: $-2315.12
#         Greatest Increase in Profits: Feb-2012 ($1926159)
#         Greatest Decrease in Profits: Sep-2013 ($-2196167)


# Let s Import our modules 
import os
import csv

#let s declare our variables which will contain values
date = []
profit_loss = []

# Create a file path across the operating system
csvpath = os.path.join ('Resources', 'budget_data.csv')

 # open the file
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])
        print(row)

    
    
    





