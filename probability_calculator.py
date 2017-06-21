#import numpy as np
from fractions import Fraction
#This is going to be have wavy
#But here is a transition matrix that represents the probabilities to get from X matching rolls to Y matching rolls

class probability_wrapper():
  def __init__(self, p_v):
    self.p_v = p_v

  def item(self, i):
    return self.p_v[0][i]

  def to_string(self):
     return str(self.p_v)

#How is this matrix used?
#Lets say we have a pair, and we want to know the chance of rolling a yahtzee next turn
#pair is represnted by the mat [0,1,0,0,0]
#Multiply the 'pair' matrix by the trans_mat, and you get a vector of length 5
#the value in the second index is the probability of still only having a pair after rerolling
#The value in the third index is the probability of having triples after rerolling
trans_mat = [[120.0/1296.0, 900.0/1296.0, 250.0/1296.0, 25.0/1296.0, 1.0/1296.0],
             [0, 120.0/216.0, 80.0/216.0, 15.0/216.0, 1.0/216.0],
             [0, 0, 25.0/36.0, 10.0/36.0, 1.0/36.0],
             [0, 0, 0, 5.0/6.0, 1.0/6.0],
             [0, 0, 0, 0, 1]]


def compute_probabilities(number_already_matching, rolls_left, debug = False):
    #this is a hack to avoid problems
    number_already_matching = min(1, number_already_matching)

    #this matrix will start as an identity
    probability_vector = [[0,0,0,0,0]]
    probability_vector[0][number_already_matching-1] = 1
 
    if debug: print probability_vector
    

    #Multiply this matrix by the trans mat to get probabilites of ending with X 'good' dice
    #Do the multiplication once for each roll we have left
    for i in range(rolls_left):
        probability_vector = matrixmult(probability_vector, trans_mat)

    if debug: print probability_vector

    return probability_wrapper(probability_vector)

def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print "Cannot multiply the two matrices. Incorrect dimensions."
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    compute_probabilities(1,2, True)
