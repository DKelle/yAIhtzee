from hand import hand

class fours(hand):
  
  def get_points(self, dice):
    return 4 * dice.count(4)

  def get_hand_name(self):
    return "fours"

  def get_weight(self, dice):
    #what would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)

    #which dice would we re roll if we wanted to go for fours?
    reroll = [i for i, x in enumerate(dice) if not x == 4]

    #how many dice are not fours?
    not_fours = len(reroll)

    #how many fours do we expect to roll, if we re roll our non-fours?
    expected_fours = not_fours * self.sixth

    #what is our expected score?
    return (cur + expected_fours)/24, reroll
