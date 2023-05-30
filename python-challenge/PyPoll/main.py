# begin from here-------i have taken help code from our instructor
#

import  csv

# csv_path = "Resources/election_data.csv"
# my file path ------
csv_path = "PyPoll/Resources/election_data.csv"

votes = 0

candidates = {}

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)

        votes += 1

        # get the candidate
        # if the candidate is in the dictionary, we want to add 1 to the value
        # else, init with a vote of one

        candidate = row[2]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

print(votes)
print(candidates)

for key in candidates:
    print(key, 100*candidates[key]/votes)
print(max(candidates, key=lambda x: candidates[x]))

# ouput to a file
f = open("PyPoll/analysis/PyPollResult.txt", "w")
print("Total Votes: ",votes, file=f),
print("candidates : ", candidates, file=f),
#key_x =key, 100*candidates[key]/votes
#print("key", key_x, file=f)
winner_x = max(candidates, key=lambda x: candidates[x])
print("Winner : ", winner_x, file=f)
# last line ----only for reference