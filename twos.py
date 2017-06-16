from hand import hand

class twos(hand):
  
  def get_points(self, dice):
    return 2 * dice.count(2)

  def get_hand_name(self):
    return "twos"

  def get_weight(self, dice):
    #what would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)

    #which dice would we re roll if we wanted to go for twos?
    reroll = [i for i, x in enumerate(dice) if not x == 2]

    #how many dice are not twos?
    not_twos = len(reroll)

    #how many twos do we expect to roll, if we re roll our non-twos?
    expected_twos = not_twos * self.sixth

    #what is our expected score?
    return (cur + expected_twos)/12, reroll
