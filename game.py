from random import randint
from three_of_a_kind import three_of_a_kind
from four_of_a_kind import four_of_a_kind
from full_house import full_house
from small_straight import small_straight
from large_straight import large_straight
from upper_section_hand import upper_section_hand
from yahtzee import yahtzee
from chance import chance

debug = True 
dice = [0,0,0,0,0]
hands = []
score = 0

def init_hands():
  global score
  global hands
  hands = []
  score = 0
  hands.append(upper_section_hand(1))
  hands.append(upper_section_hand(2))
  hands.append(upper_section_hand(3))
  hands.append(upper_section_hand(4))
  hands.append(upper_section_hand(5))
  hands.append(upper_section_hand(6))
  hands.append(three_of_a_kind())
  hands.append(four_of_a_kind())
  hands.append(full_house())
  hands.append(small_straight())
  hands.append(large_straight())
  hands.append(yahtzee())
  hands.append(chance())


def take_turn():
  global score
  global dice

  #start the turn by randomizing rolling all dice
  for i in range(len(dice)):
    dice[i] = roll()
  if debug: print 'rolled: ' + str(dice)

  #get_best_hand() will calculate expected scores, and which dice would be best to reroll
  projected_best, reroll_list = get_best_hand(dice)
  dice = reroll_dice(dice, reroll_list)
  if debug: print 'rolled: ' + str(dice)
  
  #reroll one more time
  projected_best, reroll_list = get_best_hand(dice)
  dice = reroll_dice(dice, reroll_list)
  if debug: print 'rolled: ' + str(dice)

  score += take_hand(dice)

def get_best_hand(dice):
  #Get all the hands that we can still take
  hands_available = [i for i in hands if not i.is_taken()]
  number_available = len(hands_available)

  if debug: print 'about to analyze projected scores for this roll'

  #To decide which move we will take, we need to see what is going to maximize our score
  #To get a 'projected game score', take the actual number of points we will get for some hand
  # and then add to it the average number of points all of the other hands would give
  # for example, on average, we will probably get 2.5 points for taking ones (meaning taking 1 point for ones would be a bad move)
  projected_score_list = [0] * number_available
  for j in range(len(projected_score_list)):
    if debug: print '\tIf we take ' + hands_available[j].get_hand_name()

    #Taking 'weight' represents accepting this hand
    #Taking 'average score' represents taking this hand at some later point
    
    for i, h in enumerate(hands_available):
      #This array will our projected score, if we take each hand still available
      projected_hand = 0
      if i == j:
        weight, reroll = h.get_weight(dice)
        projected_hand = weight
      else:
        projected_hand = h.get_average_score()

      projected_score_list[j] += projected_hand

      if debug: print '\t\t' + h.get_hand_name() + ':' + str(projected_hand)
    if debug: print '\tTotal projected score: ' + str(projected_score_list[j])

  #What is our max projected score?
  max_projected = max(projected_score_list)
  
  #Which hand gave us this projected score?
  best_hand_index = projected_score_list.index(max_projected) 
  best_hand = hands_available[best_hand_index]

  if debug: print 'the best projected score comes from ' + best_hand.get_hand_name()
  
  #now that we know the best hand, what dice do we need to reroll?
  weight, reroll = best_hand.get_weight(dice)    
  if debug: print 'about to re roll dice ' + str(reroll)

  #We want to return the hand that yeilds the highest projected score, and the dice that we'd need to reroll
  return best_hand, reroll



def roll():
  return randint(1,6)

def reroll_dice(dice, reroll):
  dice = [roll() if i in reroll else dice[i] for i in range(len(dice)) ]
  return dice

  
def take_hand(dice):
  #Get all the hands that we can still take
  hands_available = [i for i in hands if not i.is_taken()]
  number_available = len(hands_available)

  #To decide which move we will take, we need to see what is going to maximize our score
  #To get a 'projected game score', take the actual number of points we will get for some hand
  # and then add to it the average number of points all of the other hands would give
  # for example, on average, we will probably get 2.5 points for taking ones (meaning taking 1 point for ones would be a bad move)
  projected_score_list = [0] * number_available
  for i, h in enumerate(hands_available):
    #Taking 'weight' represents accepting this hand
    #Taking 'average score' represents taking this hand at some later point
    
    for j in range(len(projected_score_list)):
      #This array will our projected score, if we take each hand still available
      if i == j:
        projected_score_list[j] += h.get_points(dice) 
      else:
        projected_score_list[j] += h.get_average_score()

  #What is our max projected score?
  max_projected = max(projected_score_list)
  
  #Which hand gave us this projected score?
  best_hand_index = projected_score_list.index(max_projected) 
  best_hand = hands_available[best_hand_index]

  #now that we know the best hand, what dice do we need to reroll?
  weight, reroll = best_hand.get_weight(dice)    

  #We want to return the hand that yeilds the highest projected score, and the dice that we'd need to reroll
  return best_hand.take(dice)


def run_game(db = False):
  global debug
  debug = db
  
  print '\n\n Welcome to yAIhtzee \n\n'
  init_hands()
  while False in [hands[i].is_taken() for i in range(len(hands))]:
    take_turn()
  print 'Final score: ' + str(score)
  return score

if __name__ =="__main__":
  run_game(True)