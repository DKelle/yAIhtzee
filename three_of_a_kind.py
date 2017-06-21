from lower_section_hand import lower_section_hand
import probability_calculator as pc

class three_of_a_kind(lower_section_hand):


  def get_points(self, dice):
    if max(self.get_occurance_list(dice)) >= 3:
      return sum(dice)
    return 0

  def get_hand_name(self):
    return "three of a kind"

  def get_weight(self, dice, rolls_left):
    debug = False
    if debug: print dice

    #What is the greatest number of common dice we have?
    occurance_list = self.get_occurance_list(dice)
    occurances = max(occurance_list)

    #what is the face value of the dice that we have the most occurances of?
    common_roll = occurance_list.index(occurances)
    if debug: print 'have mostly ' + str(common_roll)

    #which dice would we want to re roll if we are going for three of a kind?
    reroll = [i for i, x in enumerate(dice) if not x == common_roll]

    if debug:
      print 'if going for 3 of a kind, would reroll ' + str(reroll)

    #Get the probability vector of rolling more 'good' dice
    probabilities = pc.compute_probabilities(occurances, rolls_left)

    if debug: print 'probabilities are ' + str(probabilities)

    #Now that we know the probabilites, what is our expected score?
    exp_score = 0
    for i in range(2,len(dice)):
        if debug: print 'adding to score ' + str((((i+1) * common_roll) + ((5-i-1) * 2.5 )) * probabilities.item(i))
        exp_score += (((i+1) * common_roll) + ((5-i-1) * 2.5 )) * probabilities.item(i)

    if debug: print 'exp is ' + str(exp_score)

    return exp_score, reroll

  def get_average_score(self):
    return 30
