from hand import hand

class threes(hand):
  
  def get_points(self, dice):
    return 3 * dice.count(3)

  def get_hand_name(self):
    return "threes"

  def get_weight(self, dice):
    #what would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)

    #which dice would we re roll if we wanted to go for threes?
    reroll = [i for i, x in enumerate(dice) if not x == 3]

    #how many dice are not threes?
    not_threes = len(reroll)

    #how many threes do we expect to roll, if we re roll our non-threes?
    expected_threes = not_threes * self.sixth

    #what is our expected score?
    return cur + expected_threes, reroll
