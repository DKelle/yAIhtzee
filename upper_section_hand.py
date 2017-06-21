from hand import hand
import probability_calculator as pc

class upper_section_hand(hand):

  def __init__(self, value):
    self.taken = False
    self.sixth = 1.0/6.0
    self.value = value
    self.hand_name_dict = {1:"ones", 2:"twos", 3:"threes", 4:"fours", 5:"fives", 6:"sixes"}

  def get_points(self, dice):
    return self.value * dice.count(self.value)

  def get_weight(self, dice, rolls_left):
    debug = False

    if debug:
        print dice
        print 'going for ' + str(self.value)

    #How many 'good' dice do we already have?
    good = max(dice.count(self.value), 1)

    #Which dice would we want to reroll?
    reroll = [i for i, x in enumerate(dice) if not x == self.value]
    number_to_reroll = len(reroll)

    #Get a matrix representing the probability of ending up with 1, 2, 3, 4 or 5 'good' dice
    probabilities = pc.compute_probabilities(good, rolls_left)

    if debug: print probabilities

    #Now that we know the probability of ending up with 1, 2, 3, 4, or 5 'good' dice, what is our exp score?
    exp_score = 0
    for i in range(len(dice)):
        #probability of one 'good' times value of one 'good' + probability of two * value of two etc...
        if debug: print 'adding to score : ' + str((i+1) * self.value * probabilities.item(i))
        exp_score += (i+1) * self.value * probabilities.item(i)

    if debug: print 'exp is ' + str(exp_score)

    return exp_score, reroll

  def get_hand_name(self):
    return self.hand_name_dict[self.value] if self.value in self.hand_name_dict else "NONE"

  def get_average_score(self, hands_left):
    return 2.5 * self.value
