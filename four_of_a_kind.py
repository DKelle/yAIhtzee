from lower_section_hand import lower_section_hand
import probability_calculator as pc

class four_of_a_kind(lower_section_hand):


  def get_points(self, dice):
    if max(self.get_occurance_list(dice)) >= 4:
      return sum(dice)
    return 0

  def get_hand_name(self):
    return "four of a kind"

  def get_weight(self, dice, rolls_left):
    debug = False
    if debug: print dice

    #What is the greatest number of common dice we have?
    occurance_list = self.get_occurance_list(dice)
    occurances = max(occurance_list)

    #what is the face value of the dice that we have the most occurances of?
    common_roll = occurance_list.index(occurances)
    if debug: print 'have mostly ' + str(common_roll)

    #which dice would we want to re roll if we are going for four of a kind?
    reroll = [i for i, x in enumerate(dice) if not x == common_roll]

    if debug:
      print 'if going for 4 of a kind, would reroll ' + str(reroll)


    #Get the probability vector of rolling more 'good' dice
    probabilities = pc.compute_probabilities(occurances, rolls_left)

    if debug: print 'probabilities are ' + str(probabilities)

    #Now that we know the probabilities, what is our expected score?
    exp_score = 0
    for i in range(3, len(dice)):
      if debug: print 'adding to score ' + str((((i+1) * common_roll) + ((5-i-1) * 2.5 )) * probabilities.item(i))
      exp_score += (((i+1) * common_roll) + ((5-i-1) * 2.5 )) * probabilities.item(i)

    if debug: print 'exp score is ' + str(exp_score)

    return exp_score, reroll


  def get_average_score(self):
    return 40
