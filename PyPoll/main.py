# import modules
import os
import csv

# path to file
csvpath = os.path.join('Resources', 'election_data.csv')

# create variable lists
candidates = []
country = []
voter_id = []

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# open file, and read it
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader) #skip first line for iteration, call it header

#    print(header)

    # iterate through the file, line by line, populating lists with values from column1 and 2
    for row in csvreader:
        voter_id.append(row[0])
        country.append(row[1])
        candidates.append(row[2])
    
    # The total number of votes cast
    total_votes = len(voter_id)
    
    # A complete list of candidates who received votes
    unique_candidates = list(set(candidates))
    
    # The percentage of votes each candidate won
    khan_votes_p = candidates.count('Khan') / total_votes * 100
    correy_votes_p = candidates.count('Correy') / total_votes * 100
    li_votes_p = candidates.count('Li') / total_votes * 100
    otooley_votes_p = candidates.count("O'Tooley") / total_votes * 100

    # The total number of votes each candidate won
    khan_votes_t = candidates.count('Khan')
    correy_votes_t = candidates.count('Correy')
    li_votes_t = candidates.count('Li')
    otooley_votes_t = candidates.count("O'Tooley")

    # The winner of the election based on popular vote
    # make a dictionary out of zipping two lists key_candidates and values_votes_t, find max
    key_candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    values_votes_t = [khan_votes_t, correy_votes_t, li_votes_t, otooley_votes_t]
    candidates_and_votes_dict = dict(zip(key_candidates, values_votes_t))
    winner = max(candidates_and_votes_dict, key=candidates_and_votes_dict.get)

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

# create file to print on terminal window
print_file = (f"  Election Results \n"
      f"  -------------------------\n"
      f"  Total Votes: {total_votes}\n"
      f"  -------------------------\n"
      f"  Khan: {'{:.2f}'.format(khan_votes_p)}% ({khan_votes_t})\n"
      f"  Correy: {'{:.2f}'.format(correy_votes_p)}% ({correy_votes_t})\n"
      f"  Li: {'{:.2f}'.format(li_votes_p)}% ({li_votes_t})\n"
      f"  O'Tooley: {'{:.2f}'.format(otooley_votes_p)}% ({otooley_votes_t})\n"
      f"  -------------------------\n"        
      f"  Winner: {winner}\n"
      f"  -------------------------\n")
print(print_file)

# create output file for the analysis report
output_file = os.path.join("Election_Results.txt")

with open('Election_Results.txt', 'a') as the_file:
    the_file.write(print_file)
