from random import randint
from random import random

# Approach.py


# This program uses reinforcement learning to determine the optimal policy
# for Approach.
# Recall that approach works like this:
# Both players agree on a limit n.
# Player 1 rolls first. They go until they either exceed n or hold.
# Then player 2 rolls. They go until they either exceed n or beat player 1's score.
# The player who is closest to n without going over wins.
# Note:
# We can reduce this to the problem of player 1 choosing the best value at which to hold.
# This is called a policy; once we know the best number to hold at, we can act optimally.


def approach(n) :
    q_table = [[random() / 100.0, random() / 100.0] for i in range(n)]

    for i in range(100000) :
        # Select an initial state.
        # Take the best move with p=epsilon, and the worst move with p=1-epsilon.
        # Continue playing until the game is done.
        # If you win, reward = 1.
        # If you lose, reward = 0.
        ## Use Q-learning to update the q-table for each state-action pair visited.

    ## After 100000 iterations, print out your q-table.