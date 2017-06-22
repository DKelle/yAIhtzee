from lower_section_hand import lower_section_hand

class chance(lower_section_hand):

  def get_points(self, dice):
    return sum(dice)

  def get_hand_name(self):
    return "Chance"

  def get_weight(self, dice, rolls_left):
    debug = False

    #Lets decide to reroll everything under 4
    reroll = [i for i, x in enumerate(dice) if x <= 3]
    number_to_reroll = len(reroll)

    if debug: print dice
    if debug: print 'rerolling ' + str(reroll)

    #Total the value of all dice 4,5 or 6
    keep = [i for i in dice if i >= 4]
    cur = sum(keep)

    if debug: print 'keeping the following values ' + str(keep)
    if debug: print 'the value of the dice we are keepig: ' + str(cur)

    #assume on average we will get 3.5 for each dice we reroll
    exp_score = cur + 3.5 * number_to_reroll

    #There is a 50% chance to get the average roll (3.5)
    weight = .5 * exp_score

    return weight, reroll

  def get_average_score(self, hands_left):
    #FIXME
    #This isn't great, but nor now let's just say that the average chance score is 3 points * 5 dice = 15
    return 15
