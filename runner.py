import subprocess
import numpy as np
from matplotlib import pyplot as plt
from game import run_game
from scipy.stats import binned_statistic


if __name__ == "__main__":

  #Do we need to warn user to commit before we run these tests?
  #If any of the following files have non-commited changes, we need to warn user
  important_files = ['full_house','large_straight','small_straight','three_of_a_kind', 'four_of_a_kind', 'chance', 'upper_section_hand', 'yahtzee']
  uncommited_if = []

  #We use commit shas to identify what version achieved a given score
  #Make sure our changes are in a new commit, so we attach correct IDs to scores
  status_label = subprocess.check_output(["git", "status"])
  status_lines = status_label.split('\n')

  #Get all the non-commited files. See if any of them are important files
  for line in status_lines:
    if 'modified' in line:
      for i_f in important_files:
        if i_f in line:
          uncommited_if.append(i_f)

  #Are we going to continue with the run, or warn user and bomb out?
  if len(uncommited_if) > 0:
    print 'Please commit the following files before running!'
    for f in uncommited_if:
      print '\t' + str(f)

  #Cool, we have all files commited. Let's get some averages!
  else:
    scores = []

    #Get our latest commit hash so we can label the output
    label = subprocess.check_output(["git", "log"])
    commit = label.split("\n")[0].split()[1]

    #Calculate a 500 game average
    total = 0
    games = 500
    for i in range(games):
      score = run_game(db = False)
      scores.append(score)
      total += score
    total /= games

    #Construct the result string
    result = commit + ' has a 500 game average of ' + str(total) + ' \n'

    #before we write in the result, read the results file so we can update the 'Best commit' line at the end
    with open("results.txt", "r") as f:
      lines = f.readlines()

    #Create a list of (score, commit) pairs
    score_list = []
    for line in lines[:-1]:
      words = line.split()
      if len(words) > 1:
        commit = words[0]
        score = int(words[-1].rstrip())
        score_list.append((score,commit))

    #Don't forget to add this game to the results
    score_list.append((total, commit))

    #sort this list to tell which commit did the best
    score_list = sorted(score_list)

    #Construct the line that says which commit was best
    winning_pair = score_list[-1]
    winning_commit = winning_pair[-1] + ' had the highest score of ' + str(winning_pair[0])

    #Cut off the line that said the previous winner
    lines = lines[:-1]
    lines.append(result)
    lines.append(winning_commit)

    with open("results.txt", "w") as f:
      for line in lines:
        f.write(line)

    #Also print this games result, so user doesn't /have/ to open results.txt
    print result

    #print out information about the distribution of scores
    bins = []
    for i in range(0,300, 10):
     #Count the number of scores that were in the range i-i+10
     bins.append(len([s for s in scores if s < (i+10) and s >= i]))

    #Now that we have the bins, lets print a pretty graph
    for i, x in enumerate(bins):
      print str(i*10) + '\t|' + ('*'*x)

