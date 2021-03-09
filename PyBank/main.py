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
p_l_change = []
total_rows = 0
total_sum = 0
change  = 0
previous = 0

max_inc = 0
max_date = ""

max_dec = 0
min_date = ""

# Create a file path across the operating system
csvpath = os.path.join ('Resources', 'budget_data.csv')

 # open the file
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

# let s store our data in list
    for row in csvreader:
        total_rows=total_rows + 1
        total_sum  =total_sum + int(row[1])
        change = int(row[1])- previous
        #  o/p of line 44 is 867884 - 0, 986770-867884
        p_l_change.append(change)
        previous = int(row[1])

        if change > max_inc:
            max_inc = change
            max_date = row[0]

        if change < max_dec:
            max_dec = change
            min_date = row[0]

    avg_change = sum(p_l_change[1:])/len(p_l_change[1:])
    avg_change = "%.2f" % avg_change
    # let s print the output

    
    print("Financial Analysis")
    print ("----------------------------------------")
    print(f"Total Months : {total_rows}")
    print(f"Total Amount : $ {total_sum}")
    print(f"change : $ {avg_change}")
    print(f'Greatest Increase in Profits : {max_date}' ,"($", max_inc ,")")
    print(f'Greatest Decrease in Profits : {min_date}' ,"($", max_dec ,")")


#Specify the file to write to
output_file = os.path.join("Analysis","output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------------------\n")
    textfile.write(f"Total Months : {total_rows}\n")
    textfile.write(f"Total Amount : $ {total_sum}\n")
    textfile.write(f"change : $ {avg_change}\n")
    textfile.write(f"Greatest Increase in Profits : {max_date} ($ {max_inc})\n")
    textfile.write(f"Greatest Decrease in Profits : {min_date} ($ {max_dec})\n")



