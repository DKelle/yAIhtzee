from lower_section_hand import lower_section_hand

class small_straight(lower_section_hand):

  def get_points(self, dice):
    sequence = len(get_max_sequence(dice))

    if sequence >= 4:
      return 30
    return 0

  def get_max_sequence(self, dice):
    dice = sorted(dice)
    rl = {}
    best_range = xrange(0)
    for x in dice:
        run = rl[x] = rl.get(x-1, 0) + 1
        r = xrange(x-run+1, x+1)
        if len(r) > len(best_range):
            best_range = r
    return list(best_range)

  def get_hand_name(self):
    return "Small straight"

  def get_weight(self, dice):
    debug = True
    max_sequence = self.get_max_sequence(dice)
    if debug: print dice    
    if debug: print max_sequence
    









    value_occurances_max, value_occurances_second = self.get_max_occurances(dice)

    if debug:
      print dice
      print value_occurances_max 
      print value_occurances_second

    #How many do we still need to form our 3 of a kind?
    need_for_three = 3 - min(3, value_occurances_max[-1])

    #How many do we still need to form our pair?
    need_for_two = 2 - value_occurances_second[-1]

    if debug: print 'need for three: ' + str(need_for_three) 
    if debug: print 'need for two: ' + str(need_for_two) 

    #How many dice are we rerolling?
    number_to_reroll = need_for_three + need_for_two

    #which dice are we rerolling?
    reroll = [i for i, x in enumerate(dice) if x not in [value_occurances_max[0], value_occurances_second[0]]]
    
    #if we have rolled 4 of something, we only want to keep 3 out of those 4
    if value_occurances_max[-1] >= 4:
      reroll.append(dice.index(value_occurances_max[0]))

    if debug: print 'rerolling ' + str(reroll)

    if debug: print 'number to reroll: ' + str(number_to_reroll)

    #What are the odds of rerolling these dice, and completing our full house?
    chance_of_three = self.sixth ** need_for_three
    chance_of_two = self.sixth ** need_for_two
    chance_of_both = chance_of_three * chance_of_two

    if debug:
      print 'chance of three: ' + str(chance_of_three)
      print 'chance of two: ' + str(chance_of_two)
      print 'chance of both: ' + str(chance_of_both)


    #How many different ways are there for us to complete our full house?
    ways = self.ncr(number_to_reroll, need_for_three)

    if debug: print 'number of ways ' + str(ways)
    
    #The probability of rolling a full house is thus
    probability = chance_of_both * ways
    
    if debug: print 'total prob: ' + str(probability)

    #A full house is worth 25 - weight becomes 25 * our chance of getting a full house
    weight = 25 * probability

    return weight, reroll 

