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
    epsilon = 0.1
    q_table = [[random() / 100.0, random() / 100.0] for i in range(n)]
    print(q_table)
    best_action = 0

    for i in range(100000) :
        # Select an initial state.
        s = randint(1, 6)

        while True:
            # Take the best move with p=epsilon, and the worst move with p=1-epsilon.
            if random() > epsilon:
                action = 0 if q_table[s][0] > q_table[s][1] else 1
            else:
                action = 0 if q_table[s][0] < q_table[s][1] else 1

            ran_num = s + randint(1, 6)
            if ran_num < n and action == 0:
                s = ran_num
            else:
                reward = 1 if s == 0 or s >= n else 0
                break

        q_table[s][action] += 0.1 * (reward + (0.8 * best_action) - q_table[s][action])
        best_action = q_table[s][action]

    print("sum:   roll     hold   [action]")
    for i in range(n):
        print(f"{i}: {q_table[i][0]:.6f} {q_table[i][1]:.6f} [{['roll', 'hold'][q_table[i].index(max(q_table[i]))]}]")



approach(10)