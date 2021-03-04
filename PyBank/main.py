#Import the modules
import os
import csv

#Create a file path across the operating system
csvpath = os.path.join('PyBank', 'resources', 'budget_data.csv')

#open the file using csv module
with open(csvpath) as csvfile:
    #create csvreade object to specify delimiter and variable that holds contents 
    csvreader = csv.reader(csvfile, delimiter=',')
    #check to see if read file works
    print(csvreader)

    #Since we have headers, read header row by creating header object 
    csv_header = next(csvreader)
    print(f"csv Header : {csv_header}")

    #read each row of data after the header
    for row in csvreader
        print(row)
        
