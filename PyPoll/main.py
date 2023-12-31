# import dependencies 
import os
import csv

# grabbing the election data from the resources folder 
Election_Data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')

# number of rows, excluding header 
Total_Votes = 0 

# creating an open dictionary 
Votes_Per_Candidate = {}

# opeping election_data
with open(Election_Data_csv, newline='') as csvfile:

    # delimiter separates text strings with a comma  
    csvreader = csv.reader(csvfile, delimiter=',')

    # reading the headder row 
    csv_header = next(csvreader)

    # next, read all of the rows 
    for row in csvreader:
        Total_Votes += 1
        if row[2] not in Votes_Per_Candidate:
            Votes_Per_Candidate[row[2]] = 1
        else:
            Votes_Per_Candidate[row[2]] += 1   
           
# print

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes))
print("-------------------------")

for candidate, votes in Votes_Per_Candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/Total_Votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(Votes_Per_Candidate, key=Votes_Per_Candidate.get)

print(f"Winner: {winner}")

# output file 

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(Total_Votes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in Votes_Per_Candidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/Total_Votes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')


