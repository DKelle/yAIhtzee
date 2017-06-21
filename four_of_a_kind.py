from lower_section_hand import lower_section_hand

class four_of_a_kind(lower_section_hand):


  def get_points(self, dice):
    if max(self.get_occurance_list(dice)) >= 4:
      return sum(dice)
    return 0

  def get_hand_name(self):
    return "four of a kind"

  def get_weight(self, dice):
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

    #How many dice are we wanting to re-roll?
    bad_die = len(reroll)

    #
    #What is the chance we get a four of a kind if we re-roll these dice?
    #

    #4 - 'the number of good we already have' is the number of 'good' rolls we need to get a 4 of a kind
    good_still_needed = max(0, 4-occurances)
   
    #bad_die - 'good_still_needed' is how many 'bad rolls' we can allow and still get the three of a kind
    bad_allowed = bad_die - good_still_needed

    #What is the chance of rolling exactly the number of good we need, and exactly the number of bad we can allow?
    chance_of_good = self.sixth ** (good_still_needed + 0.0)
    chance_of_bad = (1.0-self.sixth) ** bad_allowed
    chance_of_both = chance_of_good * chance_of_bad

    if debug: print 'chance of good: ' + str(chance_of_good)
    if debug: print 'chance of bad: ' + str(chance_of_bad)
    if debug: print 'chance of both: ' + str(chance_of_both)

    #How many different ways are there to end up with X good, and Y bad? good_still_needed choose reroll
    ways = self.ncr(len(reroll), good_still_needed)

    if debug: print 'ways: ' + str(ways)

    #Now, what is the overall chance of getting X good and Y bad?
    probability = ways * chance_of_both

    if debug: print 'total prob: ' + str(probability)

    #What would our score be if we did get the four of a kind?
    total_score = (common_roll * 4) +  3 #3 because on average let's assume the other dice is a three

    if debug: print 'total score would be ' + str(total_score)
    if debug: print 'total weight would be ' + str((probability*total_score))
    
    #what is our expected score?
    return (probability * total_score), reroll


  def get_average_score(self):
    return 40
