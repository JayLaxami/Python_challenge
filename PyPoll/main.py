#import os and csv file
import os
import csv

#Assigning variables(list for candidate number and dictionary for candidate votes)
total_votes = 0
list_of_candidates = []
vote_count = {}
vote_percentage = {}

#csv path
csvpath = os.path.join("C:/Users/juhis/Python_challenge/PyPoll/", "Resources", "election_data.csv")

#Read and open csv path with header
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#for loop to find votes  
    for row in csvreader:
        total_votes = total_votes + 1
        
#Condition for appending in list of candidates and vote count         
        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])
            vote_count[row[2]] = 0

        vote_count[row[2]] += 1
        
    for candidate in list_of_candidates:
        vote_percentage[candidate] = round((vote_count[candidate]/sum(vote_count.values()))*100,3)


print(total_votes, list_of_candidates, vote_count, 
          max(vote_count, key=vote_count.get), vote_percentage, sep = "\n")

#For loop to get output of vote percentage and count for all three candidates
result = {}
for candi in list_of_candidates:
    result[candi] = str(vote_percentage[candi]) + "%" + " " + "(" + str(vote_count[candi]) + ")"

candidate_out = "\n".join(f"{key}: {value}" for key,value in result.items())

#Write the output in text file of Analysis folder
output = (
    f"Election Results\n" 
    f"...................\n"
    f"Total Votes: {total_votes}\n" 
    f"..........................\n"
    f"{candidate_out}\n"
    f".................................\n"
    f"Winner: {max(vote_count, key= vote_count.get)}\n"
    f".................................."
    )
    
output_path= os.path.join("Analysis", "election_analysis.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(output)