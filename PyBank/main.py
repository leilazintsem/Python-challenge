Pseudocode for PyBank Question
# we have some data which are store somwhere
# data store in a cvs file
#we are being asked to create script/manipulate the data contained in csv file 
# to come up with specific script
    # to achieve that, I need to do some math
        # the specific output should look like the following

        Financial Analysis
----------------------------
        Total Months: 86
        Total: $38382578
        Average  Change: $-2315.12
        Greatest Increase in Profits: Feb-2012 ($1926159)
        Greatest Decrease in Profits: Sep-2013 ($-2196167)
# Import the modules
import os
import csv

#Create a file path across the operating system
csvpath = os.path.join ('Resources', 'budget_data.csv')

#open the file using csv module
with open(csvpath) as csvfile:
    #create csvreade object to specify delimiter and variable that holds contents 
    csvreader = csv.reader(csvfile, delimiter=',')
    #check to see if read file works
    print(csvreader)

    # #Since we have headers, read header row by creating header object 
    # csv_header = next(csvreader)
    # print(f"csv Header : {csv_header}")

    # #read each row of data after the header
    # for row in csvreader:
    #     print(row)

#Calculate the total month
    #total_months = 0 
#for months in csvreader
    #total_months = total_months + 1
    #print(total_months)
