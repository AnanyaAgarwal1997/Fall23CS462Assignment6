from collections import defaultdict
import random


## transitions
## The transition probabilities are stored in a dictionary mapping (state, action) pairs to a list
## of edges - (tuples indicating destinations and probabilities)

class MDP :

    def __init__(self,gamma=0.8, error=0.01, mapfile=None, reward=-0.04):
        self.gamma=gamma
        self.error=error
        self.reward=reward
        if mapfile :
            self.goals, self.transition_probs = load_map_from_file(mapfile)
        else :
            self.goals = []
            self.transition_probs=defaultdict(list)
        self.states =  set([item[0] for item in self.transition_probs.keys()] + [item[0] for item in self.goals])
        self.actions = set([item[1] for item in self.transition_probs.keys()])
        self.utilities = defaultdict(float)
        for item in self.states :
            self.utilities[item] = 0.1
        for item in self.goals :
            self.utilities[item[0]] = float(item[1])


    def __repr__(self):
        return f"Gamma: {self.gamma}, Error: {self.error}, Reward: {self.reward}, Goals: {self.goals}, Transitions: {self.transition_probs}, States: {self.states}, Actions: {self.actions}"

    ## return the policy, represented as a dictionary mapping states to actions, for the current utilities.
    ## you do this.
    def computePolicy(self):
        policy = {}
        for  state  in self.states:
            best_action = self.computeEU(state)[1]
            policy[state] = best_action
        return policy

    ## for a state, compute its expected utility
    def computeEU(self, state):
        ## are we at a goal?
        for goal in self.goals :
            if state == goal[0] :
                return goal[1]
        ## if not, for each possible action, get all the destinations and compute their EU. keep the max.
        best_action = None
        best_eu = -1.0
        for action in self.actions :
            eu = 0.0
            destinations = self.transition_probs[(state, action)]
            for d in destinations :
                utility_value = self.utilities[d[1]] if not isinstance(self.utilities[d[1]], (list, tuple)) else self.utilities[d[1]][0]
                eu += float(utility_value) * float(d[0])
            if eu >= best_eu :
                best_action = action
                best_eu = eu
        return [float(best_eu), best_action]


    ## you do this one.
    ## 1. Initialize the utilities to random values.
    ## 2 do:
    ##     for state in states:
    ##           compute its new EU
    ##     update all values
    ##  while any EU changes by more than delta = (1-error)/error
    ##
    def value_iteration(self):
        delta = (1 - self.error) / self.error
        max_change = float('inf')
        while max_change > delta:
            max_change = 0.0
            for state in self.states:
                old_utility = self.utilities[state] if not isinstance(self.utilities[state], (list, tuple)) else self.utilities[state][0]
                new_utility = self.computeEU(state)[0]
                print(new_utility)
                max_change = max(max_change, abs(old_utility - float(new_utility)))
                self.utilities[state] = self.reward + self.gamma * new_utility

    ## you do this one.
    ## 1. Set all utilities to zero.
    ## 2. Generate a random policy.
    ## do :
    ##    given the policy, update the utilities.
    ##    call computePolicy to get the policy for these utilities.
    ## while: any part of the policy changes.

    def policy_iteration(self):
        policy_stable = False
        self.utilities = defaultdict(float)
        random_policy = {state: random.choice(list(self.actions)) for state in self.states}
        while not policy_stable:
            for state in self.states:
                self.utilities[state] = self.computeEU(state)
            new_policy = self.computePolicy()
            policy_stable = all(new_policy[state] == random_policy[state] for state in self.states)
            random_policy = new_policy


def load_map_from_file(fname) :
    goals = []
    transitions = defaultdict(list)
    with open(fname) as f:
        for line in f :
            if line.startswith("#") or len(line) < 2 :
                continue
            elif line.startswith('goals') :
                goals = [tuple(x.split(':')) for x in line.split()[1:]]
            else :
                source, action, dests = line.split(' ', 2)
                transitions[(source, action)]=[tuple(x.split(':')) for x in dests.split()]
    return goals, transitions


mdp1 = MDP(mapfile="rnGraph")
mdp2 = MDP(mapfile="2Dgraph")
mdp1.policy_iteration()
mdp1.value_iteration()