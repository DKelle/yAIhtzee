import subprocess
from game import run_game

if __name__ == "__main__":
  #Get our latest commit hash so we can label the output
  label = subprocess.check_output(["git", "log"])
  commit = label.split("\n")[0].split()[1]
  
  #Calculate a 500 game average
  total = 0
  games = 500
  for i in range(games):
    total += run_game(db = False)
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
  

