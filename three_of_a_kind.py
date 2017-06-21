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

  def get_average_score(self, hands_left):
    debug = False 

    if debug: print 'Prob of getting a ' + self.get_hand_name() + ' with only ' + str(hands_left) + ' hands left' 

    #The average score of this is the prob of getting 3s at /some point/ during this game * 12.5
    initial_vector = [1,0,0,0,0]
    probability_vector = pc.compute_probabilities(initial_vector, 2)

    if debug: print 'prob vector is ' + probability_vector.to_string()

    #probability_vector[0][0] is the prob that we will have only a singleton after 2 rerolls
    #probability_vector[0][1] is the prob thta we will have only a pair after 2 rerolls etc...
    prob = 0
    prob += probability_vector.item(2)
    prob += probability_vector.item(3)
    prob += probability_vector.item(4)

    if debug: print 'total prob is ' + str(prob)

    #Now that we know the probability of getting a 3s, what is the probability of /not/ getting it for X hands in a row?
    prob_of_one_miss = 1.0 - prob
    prob_of_X_miss = prob_of_one_miss ** hands_left

    if debug: print 'prob of not ever getting 3s this game: ' + str(prob_of_X_miss)

    #Now that we know the probability of never getting 3s for the rest of the game...
    prob_of_3s = 1.0 - prob_of_X_miss

    if debug: print 'probability of getting 3s at some point in this game ' + str(prob_of_3s)

    #12.5 comes from assuming each roll is 2.5 on average * 5 dice
    average_score = 12.5 * prob_of_3s

    if debug :print 'average score is ' + str(average_score)
   
    return average_score
