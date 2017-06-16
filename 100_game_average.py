from runner import run_game

if __name__ == "__main__":
  total = 0
  for i in range(100):
    total += run_game()
  total /= 100
  print "100 game average is: " + str(total)
