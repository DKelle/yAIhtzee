from hand import hand

class sixes(hand):
  
  def get_points(self, dice):
    return 6 * dice.count(6)

  def get_hand_name(self):
    return "sixes"

  def get_weight(self, dice):
    #what would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)

    #which dice would we re roll if we wanted to go for sixes?
    reroll = [i for i, x in enumerate(dice) if not x == 6]

    #how many dice are not six?
    not_six = len(reroll)

    #how many six do we expect to roll, if we re roll our non-six?
    expected_six = not_six * self.sixth

    #what is our expected score?
    return (cur + expected_six)/36, reroll
