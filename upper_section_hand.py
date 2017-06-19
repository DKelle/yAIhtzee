from hand import hand 

class upper_section_hand(hand):

  def __init__(self, value):
    self.taken = False
    self.sixth = 1/6
    self.value = value
    self.hand_name_dict = {1:"ones", 2:"twos", 3:"threes", 4:"fours", 5:"fives", 6:"sixes"}

  def get_points(self, dice):
    return self.value * dice.count(self.value)

  def get_weight(self, dice):
    #What would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)

    #Which dice would we re roll if we wanted to go for this hand?
    reroll = [i for i, x in enumerate(dice) if not x == self.value]

    #How many dice are "bad" rolls?
    bad_die = len(reroll)

    #How many "good rolls" do we expect if we reroll all of our "bad" dice?
    expected_good = bad_die * self.sixth

    #what is our expected score?
    return (cur + expected_good) * self.value, reroll

  def get_hand_name(self):
    return self.hand_name_dict[self.value] if self.value in self.hand_name_dict else "NONE"
