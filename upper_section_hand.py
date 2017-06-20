from hand import hand 

class upper_section_hand(hand):

  def __init__(self, value):
    self.taken = False
    self.sixth = 1.0/6.0
    self.value = value
    self.hand_name_dict = {1:"ones", 2:"twos", 3:"threes", 4:"fours", 5:"fives", 6:"sixes"}

  def get_points(self, dice):
    return self.value * dice.count(self.value)

  def get_weight(self, dice):
    debug = False 

    if debug: print dice

    #What would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)
    if debug: print 'if we go for ' + self.get_hand_name() + ' we are guarenteed ' +str(cur)

    #Which dice would we re roll if we wanted to go for this hand?
    reroll = [i for i, x in enumerate(dice) if not x == self.value]

    #How many dice are "bad" rolls?
    bad_die = len(reroll) + 0.0
    if debug: print 'We have ' + str(bad_die) + ' that would not help this hand'

    #How many "good rolls" do we expect if we reroll all of our "bad" dice?
    expected_good = (bad_die+0.0) * self.sixth
    if debug: print 'out of our bad die, we exped to roll this many good die: ' +str(expected_good)
    if debug: print self.sixth

    #what is our expected score?
    if debug: print 'expected score for ' + self.get_hand_name() + ' is ' + str((cur + expected_good*self.value))
    return cur + (expected_good * self.value), reroll

  def get_hand_name(self):
    return self.hand_name_dict[self.value] if self.value in self.hand_name_dict else "NONE"

  def get_average_score(self):
    return 2.5 * self.value
