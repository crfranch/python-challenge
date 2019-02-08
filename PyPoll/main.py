#Import modules
import os
import csv

#Read through the resource csv file titled "election_data.csv"
election_data = os.path.join("election_data.csv")

#Open the CSV File & make sure new line is an empty space
with open(election_data, 'r') as csvfile:
    #read through the csvfile and separate the three columns with a "," as the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #Initialize variable csvheader and use the next function to skip headers in csvfile
    csvheader = next(csvreader)
    
    #set each variable to an index of zero
    total_votes= 0
    candidatevotes_won= 0
    candidatevotes_lost= 0
    election_winner= 0
    #Variables for each candidate's name:
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    #Complete a list of candidates who received votes
    Candidates = ["Khan", "Correy", "Li", "O'Tooley"]

    #Use Variables and Candidates List to count number of votes each candidate received...
    for row in csvreader: 
        #Calculate total number of votes cast by counting the number of rows in the 'Voter ID' Column:
        if row[3] == Candidates[0]:
            Khan += 1
        elif row[3] == Candidates[1]:
            Correy += 1
        elif row[3]  == Candidates[2]:
            Li += 1
        else row[3] == Candidates[3]:
            OTooley += 1

    for candidate in Candidates:
        #Calculate percentage of votes each candidate won
        if candidatevotes_won = []
        #Calculate the total number of votes each candidate won



    #print(f'{candidates["name"]}')
    for i in range(len(candidatelist)):
    #The winner of the election votes based on popular vote

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
    Winner: {election_winner}'''