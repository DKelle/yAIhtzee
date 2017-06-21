from lower_section_hand import lower_section_hand
import probability_calculator as pc

class yahtzee(lower_section_hand):

  def get_points(self, dice):
    max_count = 0
    count_1 = dice.count(1)
    count_2 = dice.count(2)
    count_3 = dice.count(3)
    count_4 = dice.count(4)
    count_5 = dice.count(5)
    count_6 = dice.count(6)
    max_count = max(count_1, count_2, count_3, count_4, count_5, count_6)

    if max_count == 5:
      return 50
    return 0

  def get_hand_name(self):
    return "Yahtzee"

  def get_weight(self, dice, rolls_left):
    debug = False

    #what is the greatest number of common dice we have?
    occurance_list = self.get_occurance_list(dice)
    occurances = max(occurance_list)

    #what is the face value of the dice that we have the most occurances of?
    common_roll = occurance_list.index(occurances)

    #Which dice would we want to reroll?
    reroll = [i for i, x in enumerate(dice) if not x == common_roll]

    if debug: print 'have the most: ' + str(common_roll)

    #Now that we know how many matches we have, what are the odds of actually getting a yahtzee
    probabilities = pc.compute_probabilities(occurances, rolls_left)

    if debug: print probabilities

    #our exp scpre is 50 * our chance of getting yahtzee
    exp_score = 50 * probabilities.item(4)

    if debug : print 'exp score is ' + str(exp)

    return exp_score, reroll


  def get_average_score(self):
    return 50
