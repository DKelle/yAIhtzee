class hand:

  def __init__(self):
    self.taken = False
    self.sixth = 1.0/6.0
    self.score_taken = 0

  def set_score_taken(self, score):
    self.score_taken = score

  def get_score_taken(self):
    return self.score_taken

  def get_points(self, dice):
    pass

  def get_weight(self, dice, rolls_left):
    pass

  def get_hand_name(self):
    pass

  def reroll_which(self, dice):
    pass

  def is_taken(self):
    return self.taken

  def take(self, dice):
    self.taken = True
    points = self.get_points(dice)
    print 'Taking ' + str(points) + ' points for taking ' + self.get_hand_name() + ' with ' + str(dice)
    return points

