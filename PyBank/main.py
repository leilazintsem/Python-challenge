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

# let s store our data in list
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])
        #print(row)
    #######################################################
    # let s do the math
    #######################
    # find the total nunmber of months in the data set    
    number = len(date)
    print('Total Months :', number)

    #######################
    #find the net total amount of profit/Losses over the entire period
    total_amount = 0

    for p in profit_loss:
        total_amount = total_amount + int(p)
    print("total : ", "$" ,total_amount)


    #find the avergae of profit of the changes in profit/Losses
    #first create a find changes and create the list
    total_changes = 0

    # for i in profit_loss:
    #     changes = int(i)+ int(i+1)
    #     total_changes = total_changes + changes
    #     average = total_changes / (len(profit_loss)-1)
    #     Average = "%.2f" average
    #     print("average change : ", "$", average)








