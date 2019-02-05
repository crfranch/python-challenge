#Import modules
import os
import csv

#Pull file from following path for reading--> C:\Users\crfra\python-challenge\budget_data.csv
file = '../python-challenge/PyBank/budget_data.csv'

#For writing file:
budgetdata_csv = os.path.join("..","python-challenge","budget_data.csv")
#Absolute Path Name (For Reference) -- "C:\Users\crfra\python-challenge\PyBank\budget_data.csv"

#Open the CSV File & make sure new line is an empty space
with open(file, 'r') as csvfile:
    #read through the csvfile and split the date from the prift/losses with a "," as the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #Initialize variable csvheader and use the next function to terutn the next row of the reader's iterable object as a list
    csvheader = next(csvreader)
    
    total=0
    total_months=0
    
    #Using "csvreader" variable, create another variable to create a list, being column one of the csv "file" previsouly defined
    #convert cvsreader into a list/array
    csvreader = []
    #iterate rows within the created variable list
    for row in csvreader: 
        #Calculate the totalmonths by counting the number of elements in the array previously defined in row 20
        total_months = len(row[0])
        #alternative method - total_months == row[0]
        total_profitorloss = sum(row[1])
        #alternative method - netprofit_netloss == sum[1]
        #alternative method - csvreader.append(int(row[1]))
        avgchange = (total_profitorloss/total_months)*100
        #Alternative method - 
           #Initialize variables to calculate average change
            #previousrowamt = int(row[1])
            #averagechange = int(row[1]) - previousrowamt / (total)
        greatestincrease = int(max(row[1]))
        greatestdecrease = int(min(row[1]))

    #Print out the solution in a text file
    outputtextfile = open('budgetdata_csv', 'w')
    outputtestfile.writerow("Financial Analysis")
    outputtextfile.writerow("----------------------")
    outputtextfile.writerow("Total Months:" [total_months])
    outputtextfile.writerow("Total:" [total_profitorloss])
    outputtextfile.writerow("Average Change:" [avgchange])
    outputtextfile.writerow("Greatest Increase in Profits:" [greatestincrease])
    outputtextfile.writerow("Greatest Decrease in Profits:" [greatestdecrease])

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