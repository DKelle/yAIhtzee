from lower_section_hand import lower_section_hand

class large_straight(lower_section_hand):

  def get_points(self, dice):
    sequence = len(self.get_max_sequence(dice))

    if sequence >= 5:
      return 40
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
    return "Large straight"

  def get_probability_of_method(self, dice, goal, debug):
    #how much of what we need do we already have?
    bitmap = [1 if i in dice else 0 for i in goal]
    number_still_needed = bitmap.count(0)
    number_to_reroll = number_still_needed

    if debug:
      print 'bitmap: ' + str(bitmap)
      print 'number still needed: ' + str(number_still_needed)
      print 'number to reroll: ' + str(number_to_reroll)

    #what is the chance of rolling what we need to complete our goal?
    probability = self.sixth ** number_still_needed

    if debug:
      print 'prob  ' +str(probability)

    return probability

  def get_weight(self, dice, rolls_left):
    debug = False
    max_sequence = self.get_max_sequence(dice)
    if debug: print dice
    if debug: print max_sequence

    #there are 2 ways to get a large stright.
    # [1,2,3,4,5], [2,3,4,5,6]

    #What are the odds of getting method 1, method 2, and method 3? method 1 = (1,2,3,4)
    p_m1 = self.get_probability_of_method(dice, [1,2,3,4,5], debug)
    p_m2 = self.get_probability_of_method(dice, [2,3,4,5,6], debug)

    #out of these three methods, which are we most likely to acheive?
    max_prob = max(p_m1, p_m2)
    goal = [1,2,3,4,5] if max_prob == p_m1 else [2,3,4,5,6]
    weight = 40 * max_prob

    #Now that we know what we are going for, what do we want to re roll?
    reroll = []
    for i, x in enumerate(dice):
      if x not in goal:
        reroll.append(i)
      else:
        goal.remove(x)

    return weight, reroll

  def get_average_score(self):
    return 40
