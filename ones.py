from hand import hand

class ones(hand):
  
  def get_points(self, dice):
    return dice.count(1)

  def get_weight(self, dice):
    #what would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)

    #which dice would we re roll if we wanted to go for ones?
    reroll = [i for i, x in enumerate(dice) if not x == 1]

    #how many dice are not ones?
    not_ones = len(reroll)

    #how many ones do we expect to roll, if we re roll our non-ones?
    expected_ones = not_ones * self.sixth

    #what is our expected score?
    return cur + expected_ones, reroll

  def get_hand_name(self):
    return "ones"
