#Add our dependancies.
import csv
import os
#assign a variable to load a file from a path.
file_to_load= os.path.join("Resources/election_results.csv")
#assign a variable to save the file to a path
file_to_save= os.path.join("analysis","election_analysis.txt.")

  
#1. initialize a total vote counter
total_votes=0

#candidate options
candidate_options=[]
candidate_votes={}
#winning candidate and winning count tracker
winning_candidate= ""
winning_count=0
winning_percentage=0
#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #read the header row
    headers= next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #print the candidate name from each row
        candidate_name= row[2]
        #if the candidate does not match any exisxting candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count
            candidate_votes[candidate_name]=0
    #add a vote to that candidate's count
        candidate_votes[candidate_name]+= 1
#Determine the percentage of votes for each candidate by looping though the counts
#1. interate through the candidate list
for candidate in candidate_votes:

    # 2. retrieve vote count of a candidate
    votes= candidate_votes[candidate]
    # 3. calculate the percentage of votes
    vote_percentage=float(votes)/float(total_votes)*100
    
    #to do: print out each candidates name, vote count, and percent of votes to the terminal
    #determine winning vote count and candidate
    #determine if the votes is greater than the winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #if true then set winning_count=votes and winning_percent= vote percentage
        winning_count=votes
        winning_percentage=vote_percentage
        #and, set the winning_candidate equal to the candidate's name.
        winning_candidate= candidate
winning_candidate_summary= (
    f"-----------------\n"
    f"winner: {winning_candidate}\n"
    f"winning vote count: {winning_count:,}\n"
    f"winning percentage: {winning_percentage:.1f}%\n"
    f"----------------------\n")
print(winning_candidate_summary)
#to do : print out the winning candidate, vote count and percentage to terminal
print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")



    


