from random import randint
from ones import ones
from twos import twos
from threes import threes
from fours import fours
from fives import fives
from sixes import sixes

debug = False 
dice = [0,0,0,0,0,0]
hands = []
score = 0

def init_hands():
  global score
  global hands
  hands = []
  score = 0
  hands.append(ones())
  hands.append(twos())
  hands.append(threes())
  hands.append(fours())
  hands.append(fives())
  hands.append(sixes())

def take_turn():
  global score
  global dice

  #start the turn by randomizing rolling all dice
  for i in range(len(dice)):
    dice[i] = roll()
  if debug: print 'rolled: ' + str(dice)

  #reroll() will calculate expected scores, and which dice would be best to reroll
  dice = reroll(dice)
  dice = reroll(dice)
  score += take_hand(dice)

def reroll(dice):
  max_expected_points = -1
  dice_to_reroll = []
  #calculate our expected points for each hand, and which dice we should re roll to go for that hand
  for i, h in enumerate(hands):
    if not h.is_taken():
      exp, reroll = h.get_weight(dice)
      if exp > max_expected_points:
        max_expected_points = exp
        dice_to_reroll = reroll

  if debug: print 'about to re roll dice ' + str(reroll)

  #after we have considered all options, re roll the dice
  dice = [roll() if i in reroll else dice[i] for i in range(len(dice)) ]
  if debug: print 'Dice after roll 2: ' +str(dice)
  return dice

def roll():
  return randint(1,6)
  
def take_hand(dice):
  index = 0
  max_points = -1
  for i, h in enumerate(hands):
    if not h.is_taken():
      points = h.get_points(dice)
      if debug: print 'considering taking ' + h.get_hand_name() + ' for ' +str(points)
      if points > max_points:
        if debug: print 'this is now the current best option'
        index = i
        max_points = points

  return hands[index].take(dice)


def run_game():
  print '\n\n Welcome to yAIhtzee \n\n'
  init_hands()
  while False in [hands[i].is_taken() for i in range(len(hands))]:
    take_turn()
  print 'Final score: ' + str(score)
  return score

if __name__ =="__main__":
  run_game()
