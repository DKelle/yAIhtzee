from lower_section_hand import lower_section_hand

class full_house(lower_section_hand):


  def get_points(self, dice):
    value_occurances_max, value_occurances_second = self.get_max_occurances(dice)
    if value_occurances_max[-1] == 3 and value_occurances_second[-1] == 2:
      return 25
    return 0

  """
  def get_points(self, dice):
    sorted_dice = sorted(dice)
    sequence = 1
    max_sequence = 0
    for i in range(1,len(dice)):
      sequence = sequence + 1 if sorted_dice[i] == 1+sorted_dice[i-1] else 1
      if sequence > max_sequence:
        max_sequence = sequence

    if sequence >= 4:
      return 30
    return 0
  """


  def get_hand_name(self):
    return "Full house"

  def get_max_occurances(self, dice):
    #How many times did we roll each face value?
    occurance_list = self.get_occurance_list(dice)

    #now we need the face value of the die that we have the most, and second most of
    value_occurances_max = (0,0)
    value_occurances_second = (0,0)

    #Look at the number of occurances for each face value (1-6)
    for i in range(1,len(dice)):
      occurances = occurance_list[i]

      #Has this face value occured more often than the previous max?
      if occurances > value_occurances_max[-1]:
        #replace the current 2nd max with our now outdated max - and update max
        value_occurances_second = value_occurances_max
        value_occurances_max = (i,occurances)
      elif occurances > value_occurances_second[-1]:
        #this is not the greatest max, but it is second greatest
        value_occurances_second = (i,occurances)

    return value_occurances_max, value_occurances_second


  def get_weight(self, dice, rolls_left):
    debug = False
    if debug: print dice

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

  def get_average_score(self):
    return 25
