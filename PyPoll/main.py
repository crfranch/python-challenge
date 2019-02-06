#Import modules
import os
import csv

#Pull file from following path for reading--> C:\Users\crfra\python-challenge\budget_data.csv
#file = 'budget_data.csv'

#For writing file:
dataSet_csv = os.path.join("dataSet.csv")
#Absolute Path Name (For Reference) -- "C:\Users\crfra\python-challenge\PyBank\budget_data.csv"

#Open the CSV File & make sure new line is an empty space
with open(dataSet_csv, 'r') as csvfile:
    #read through the csvfile and split the date from the prift/losses with a "," as the delimiter
    dataSet = csv.reader(csvfile, delimiter=',')
    #Initialize variable csvheader and use the next function to terutn the next row of the reader's iterable object as a list
    csvheader = next(dataSet)
    
    total_votes=0
    candidatelist=0
    won_candidatevotes=0
    lost_candidatevotes=0
    election_winner=0
    
    #convert dataSet into a list/array
    candidatelist = []
    voteslist = []
    #iterate rows within the created variable list
    for row in dataSet: 
        #Calculate total number of votes cast
        total_votes += float(row[4])
        #Figure out list of candidates who received votes
        candidatelist.append((row[1] + " " + row[2]))
        #The percentage of votes each candidate won
        voteslist.append(row[4])

    #The total number of votes each candidate won
    #candidates = ["Khan"
     #     "Correy",
      #    "Li",
       #   "O'Tooley"]
    #print(f'{candidates["name"]}')
    for i in range(len(candidatelist)):
        print((candidatelist[i] + voteslist[i])/total_votes)
    #The winner of the election votes based on popular vote
        election_winner.pop((row[1] + " " + row[2]))

    #Print out the solution in a text file
    outputtextfile = \
    f'''Election Results
    --------------------------------
    Total Votes: {total_votes}
    --------------------------------
    Khan: {won_candidatevotes} ({total_votes})
    Correy: {lost_candidatevotes} ({total_votes})
    Li: {}
    O'Tooley: {}
    ---------------------------------
    Winner: {election_winner}
    '''

    print(outputtextfile)
    #dataSet_csv.write(outputtextfile)