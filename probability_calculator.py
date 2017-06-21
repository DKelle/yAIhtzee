import numpy as np
from fractions import Fraction
#This is going to be have wavy
#But here is a transition matrix that represents the probabilities to get from X matching rolls to Y matching rolls


#How is this matrix used?
#Lets say we have a pair, and we want to know the chance of rolling a yahtzee next turn
#pair is represnted by the mat [0,1,0,0,0]
#Multiply the 'pair' matrix by the trans_mat, and you get a vector of length 5
#the value in the second index is the probability of still only having a pair after rerolling
#The value in the third index is the probability of having triples after rerolling
trans_mat = np.mat([[120.0/1296.0, 900.0/1296.0, 250.0/1296.0, 25.0/1296.0, 1.0/1296.0],
                  [0, 120.0/216.0, 80.0/216.0, 15.0/216.0, 1.0/216.0],
                  [0, 0, 25.0/36.0, 10.0/36.0, 1.0/36.0],
                  [0, 0, 0, 5.0/6.0, 1.0/6.0],
                  [0, 0, 0, 0, 1]])


def compute_probabilities(number_already_matching, rolls_left):
    #this matrix will start as an identity
    probability_vector = np.identity(5)[number_already_matching-1]

    #Multiply this matrix by the trans mat to get probabilites of ending with X 'good' dice
    #Do the multiplication once for each roll we have left
    for i in range(rolls_left):
        probability_vector = np.dot(probability_vector, trans_mat)

    return probability_vector

if __name__ == "__main__":
    compute_probabilities(1,2)
