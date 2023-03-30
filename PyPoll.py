
import os
import csv

with open(PollData, newline = "", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimter= ",")

    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

    candilist = list()
    tally = list()
    for i in range (0,row_count):
        candidate =  data[i][2]
        tally.append(candidate)
        if candidate not in candilist:
           candilist.append(candidate)
    candicount = len(candilist)

    votes = list()
    percentage = list()
    for j in range (0,candicount)
        name = candilist[j]
        votes.append(tally,count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

    
    winner = votes.index(max(votes))


    print("Election Results")
    print("----------------------------------")
    print(f"Total Votes:{row_count:,}")
    print("-----------------------------------")
    for k in range (0,candicount):
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("-----------------------------------")
    print(f"Winner: {candilist[winner]}")
    print("-----------------------------------")

    print("Election Results", file=open("PyPoll,txt", "a"))
    print("-------------------------",file=open("PyPoll.txt","a"))
    print(f"Total Votes: {row_count:,}",file=open("PyPoll.txt","a"))
    for k in range (0,candicount) :
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("-------------------------------", file=open("PyPoll.txt","a"))
    print(f"Winner: {candilist[winner]}", file=open("PyPoll.txt","a"))
    print("-------------------------------", file=open("PyPoll.txt", "a"))
