from hand import hand

class fives(hand):
  
  def get_points(self, dice):
    return 5 * dice.count(5)

  def get_hand_name(self):
    return "fives"

  def get_weight(self, dice):
    #what would our score be if we took this hand without re rolling?
    cur = self.get_points(dice)

    #which dice would we re roll if we wanted to go for fives?
    reroll = [i for i, x in enumerate(dice) if not x == 5]

    #how many dice are not fives?
    not_fives = len(reroll)

    #how many fives do we expect to roll, if we re roll our non-fives?
    expected_fives = not_fives * self.sixth

    #what is our expected score?
    return (cur + expected_fives)/30, reroll
