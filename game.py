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
  hands.append(yahtzee())
  hands.append(chance())
  hands.append(full_house())
  hands.append(small_straight())
  hands.append(large_straight())


def take_turn():
  global score
  global dice

  #start the turn by randomizing rolling all dice
  for i in range(len(dice)):
    dice[i] = roll()
  if debug: print 'rolled: ' + str(dice)

  #get_best_hand() will calculate expected scores, and which dice would be best to reroll
  projected_best, reroll_list = get_best_hand(dice, 2)
  dice = reroll_dice(dice, reroll_list)
  if debug: print 'rolled: ' + str(dice)

  #reroll one more time
  projected_best, reroll_list = get_best_hand(dice, 1)
  dice = reroll_dice(dice, reroll_list)
  if debug: print 'rolled: ' + str(dice)

  score += take_hand(dice)

def get_best_hand(dice, rolls_left):
  #Get all the hands that we can still take
  hands_available = [i for i in hands if not i.is_taken() or "Yahtzee" in i.get_hand_name()]
  number_available = len(hands_available)

  #We are only allowed to consider Yahtzee if we haven't already taken it, or if we successfully took it already
  yahtzee_hand = [i for i in hands_available if  "Yahtzee" in i.get_hand_name()][0]
  yahtzee_taken = yahtzee_hand.is_taken()
  if yahtzee_taken:
    if not yahtzee_hand.is_successful():
      #Take out yahtzee from hands available
      hands_available = [i for i in hands if not i.is_taken()]


  if debug: print 'about to analyze projected scores for this roll'

  #There are two ways of picking the 'best' hand, either greedy, or looking ahead
  greedy = False

  #
  # GREEDY ATTEMPT
  #
  if greedy:
    max_weight = -1
    best_hand = None
    reroll = None
    for hand in hands_available:
      hand_weight, roll = hand.get_weight(dice, rolls_left)
      if hand_weight > max_weight:
        max_weight = hand_weight
        best_hand = hand
        reroll = roll

    return max_weight, reroll

  #
  # LOOK AHEAD
  #
  else:
    """ the following is a non-greedy way to choose which hand to take - doesn't work very well """
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
          weight, reroll = h.get_weight(dice, rolls_left)
          projected_hand = weight
        else:
          projected_hand = h.get_average_score(number_available)

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
    weight, reroll = best_hand.get_weight(dice, rolls_left)
    if debug: print 'about to re roll dice ' + str(reroll)

    #We want to return the hand that yeilds the highest projected score, and the dice that we'd need to reroll
    return best_hand, reroll



def roll():
  return randint(1,6)

def reroll_dice(dice, reroll):
  dice = [roll() if i in reroll else dice[i] for i in range(len(dice)) ]
  return dice


def take_hand(dice):
  #There are two ways of picking the 'best' hand, either greedy, or looking ahead
  greedy = False

  #Get all the hands that we can still take
  hands_available = [i for i in hands if not i.is_taken() or "Yahtzee" in i.get_hand_name()]
  number_available = len(hands_available)

  #We need to check if Yahtzee is actually an available hand
  #ie, If the the player has already taken one yahtzee, he does have the option to take another
  #But only if he actually has the yahtzee. You can't simply take a 0 for yahtzee if you have already taken it once
  #
  #Why would you even want to do that?
  #Roll a terrible roll, but don't want to take 0 for your 4 of a kind?
  #Take zero for that second yahtzee, you probably won't get yahtzee anyway
  yahtzee_hand = [i for i in hands if  "Yahtzee" in i.get_hand_name()][0]
  yahtzee_points = yahtzee_hand.get_points(dice)
  if not yahtzee_points > 0:
    #Take yahtzee out of the list of available hands
    hands_available = [i for i in hands if not i.is_taken()]
    number_available = len(hands_available)

  if greedy:
    max_weight = -1
    best_hand = None
    for hand in hands_available:
      hand_weight = hand.get_points(dice)
      if hand_weight > max_weight:
        max_weight = hand_weight
        best_hand = hand

    score = best_hand.take(dice)
    best_hand.set_score_taken(score)
    return score

  else:
    """ The following is a non-greedy way to pick a hand - it doesn't work bery well """
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
          projected_score_list[j] += h.get_average_score(number_available)

    #What is our max projected score?
    max_projected = max(projected_score_list)

    #Which hand gave us this projected score?
    best_hand_index = projected_score_list.index(max_projected)
    best_hand = hands_available[best_hand_index]

    #now that we know the best hand, what dice do we need to reroll?
    weight, reroll = best_hand.get_weight(dice, 0)

    #We want to return the hand that yeilds the highest projected score, and the dice that we'd need to reroll
    score = best_hand.take(dice)
    best_hand.set_score_taken(score)
    return score


def run_game(db = False):
  global score
  global debug
  debug = db

  print '\n\n Welcome to yAIhtzee \n\n'
  init_hands()
  while False in [hands[i].is_taken() for i in range(len(hands))]:
    take_turn()

  #Check to see if we get the 'upper hand bonus'
  upper_section_total = 0
  for h in hands[:6]:
    upper_section_total += h.get_score_taken()

  #If the user got more than 63 points on upper hands, they get 35 point bonus
  if upper_section_total >= 63:
    score += 35

  print 'Final score: ' + str(score)
  return score

if __name__ =="__main__":
  run_game(False)
