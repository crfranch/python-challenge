#Import modules
import os
import csv

#Pull file from following path for reading--> C:\Users\crfra\python-challenge\budget_data.csv
#file = 'budget_data.csv'

#For writing file:
budgetdata_csv = os.path.join("budget_data.csv")

#Absolute Path Name (For Reference) -- "C:\Users\crfra\python-challenge\PyBank\budget_data.csv"

#Open the CSV File & make sure new line is an empty space
with open(budgetdata_csv, 'r') as csvfile:
    #read through the csvfile and split the date from the prift/losses with a "," as the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #Initialize variable csvheader and use the next function to terutn the next row of the reader's iterable object as a list
    csvheader = next(csvreader)
    
    total=0
    total_months=0
    total_change = 0
    total_net=0
    avgchange=0
    previous_value=0
    greatestdecrease=0
    greatestincrease=0
    increase_date=0
    decrease_date=0
    
    #Using "csvreader" variable, create another variable to create a list, being column one of the csv "file" previsouly defined
    #convert cvsreader into a list/array
    #csvreader = []
    #iterate rows within the created variable list
    for row in csvreader: 
        #Calculate the totalmonths by counting the number of elements in the array previously defined in row 20
        #total_months = len(row[0])
        total_months += 1
        #total_months = total_months + 1
        #alternative method - total_months == row[0]
        total_net += int(row[1])
        #total_net = total_net + int(row[1])
        #alternative method - netprofit_netloss == sum[1]
        #alternative method - csvreader.append(int(row[1]))

        if total_months > 1:
            change = int(row[1]) - previous_value
            total_change += change
           # total_change = total_change + change
            if change > greatestincrease:
                greatestincrease = change
                increase_date = row[0]
            if change < greatestdecrease:
                greatestdecrease = change
                decrease_date = row[0]
        previous_value = int(row[1])

    #total_net = (total_profitorloss - previousrow)/(total_months - 1)
        #Alternative method - 
           #Initialize variables to calculate average change
            #previousrowamt = int(row[1])
            #averagechange = int(row[1]) - previousrowamt / (total)

    avgchange = total_change / (total_months-1)
    #Print out the solution in a text file
    outputtextfile = \
    f'''Financial Analysis
    --------------------------------
    Total Months: {total_months}
    Total: {total_net}
    Average Change: {avgchange:.2f}
    Greatest Increase in Profits: {increase_date} {greatestincrease}
    Greatest Decrease in Profits: {decrease_date} {greatestdecrease}'''

    print(outputtextfile)
   # budgetdata_csv.write(outputtextfile)

    #Alternative method to print out solution
    #outputtextfile = open('budgetdata_csv', 'w')
    #outputtextfile.writerow("Financial Analysis")
    #outputtextfile.writerow("----------------------")
    #outputtextfile.writerow("Total Months:" [total_months])
    #outputtextfile.writerow("Total:" [total_profitorloss])
    #outputtextfile.writerow("Average Change:" [avgchange])
    #outputtextfile.writerow("Greatest Increase in Profits:" [greatestincrease])
    #outputtextfile.writerow("Greatest Decrease in Profits:" [greatestdecrease])

#Additional Notes:
#Calculate Average Change for each month (current change minus previous change)
#Don't forget to add total profit with the average change?
#Calculate total months - 1, representing the amount of changes in profit, from there gather the average change    
# #Calculate Average Change for each month 
#Add total profit with the average change
#def average(TotalProfit):
#    i = 0
#    for AverageChange in TotalProfit:
#      TotalProfit == i - 1/Total_months
#   return total/len(numbers)
#   Average_change = int(total_profitorloss[1]) / total_months[0]