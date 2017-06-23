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
      if self.taken == True:
        return 100
      return 50
    return 0

  def get_hand_name(self):
    return "Yahtzee"

  def take(self, dice):
    points = self.get_points(dice)
    self.taken = True
    print 'Taking ' +str(points) + ' points for taking ' + self.get_hand_name() + ' with ' + str(dice)
    if points > 0:
      self.successful = True
    else:
      self.successful = False

    return points

  def is_successful(self):
    return self.successful

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


  def get_average_score(self, hands_left):
    debug = False

    if debug: print 'Prob of getting a ' + self.get_hand_name() + ' with only ' + str(hands_left) + ' hands left'

    #The average score of this is prob of getting yahtzee at /some point/ this game * 50
    probability_vector = pc.compute_probabilities(1, 2)

    if debug: print 'prob vector is ' + probability_vector.to_string()

    #probability_vector[0][0] is the prob that we will have only a singleton after 2 rerolls
    #probability_vector[0][1] is the prob thta we will have only a pair after 2 rerolls etc...
    prob = probability_vector.item(4)

    if debug: print 'total prob is ' + str(prob)

    #Now that we know the probability of getting yahtzee, what is the probability of /not/ getting it for X hands in a row?
    prob_of_one_miss = 1.0 - prob
    prob_of_X_miss = prob_of_one_miss ** hands_left

    if debug: print 'prob of not ever getting yahtzee this game: ' + str(prob_of_X_miss)

    #Now that we know the probability of never getting yahtzee for the rest of the game...
    prob_of_4s = 1.0 - prob_of_X_miss

    if debug: print 'probability of getting yahtzee at some point in this game ' + str(prob_of_4s)

    #12.5 comes from assuming each roll is 2.5 on average * 5 dice
    average_score = 50 * prob_of_4s

    if debug :print 'average score is ' + str(average_score)

    return average_score
