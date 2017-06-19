from hand import hand
from itertools import groupby as g
import operator as op

class lower_section_hand(hand):

  def get_occurance_list(self, dice):
    occurance_list = [dice.count(i) for i in range(7)]
    return occurance_list


  def ncr(self, n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
