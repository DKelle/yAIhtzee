import subprocess
from game import run_game

if __name__ == "__main__":
  #Get our latest commit hash so we can label the output
  label = subprocess.check_output(["git", "log"])
  commit = label.split("\n")[0].split()[1]
  
  total = 0
  games = 500
  for i in range(games):
    total += run_game(db = False)
  total /= games

  result = commit + ' has a 500 game average of ' + str(total)

  with open("results.txt", "a") as f:
    f.write(result)
  

