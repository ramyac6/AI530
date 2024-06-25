# +
import numpy as np

def evaluation(theta, gamma, pi, state_values, P, R):
    S = len(P) # num states
    A = len(P[0][0]) # num actions

    # setting some delta, that will be overwritten
    delta = np.inf
    while delta > theta:
        delta = 0
        # iterate through states
        for s in range(S):
            current_value = state_values[s]
            new_value = 0
            # for each action
            for a in range(A):
                sum_state = 0
                # determine the potential award
                for s_ in range(S):
                    sum_state = sum_state + P[s][s_][a] * (R[s][s_][a] + gamma * state_values[s_])
                new_value = new_value + pi[s][a] * sum_state
            # update
            state_values[s] = new_value
            # pick the better delta, either current or new delta
            delta = max(delta, np.abs(state_values[s] - current_value))
        return state_values
    
def improvement(gamma, pi, state_values, P, R):
    S = len(P) # num states
    A = len(P[0][0]) # num actions
    stable = True
    
    for s in range(S):
        # keep track of old actions in case the new one is worse
        prev_action = np.argmax(pi[s])
        temp = np.zeros((A))
        # for each action
        for a in range(A):
            for s_ in range(S):
                # turn it all into probabilities
                temp[s_] = temp[s_] +  P[s][s_][a] * (R[s][s_][a] + gamma * state_values[s_])
        pi[s] = temp / np.sum(temp)
        # if action is not stable and we have the same probability
        if prev_action != np.argmax(pi[s]): 
            stable = False
    return stable,pi

def pia(gamma, R, P):
    S = len(P)
    A = len(P[0][0])
    # initialize pi
    pi = np.array([[1/A]*A for i in range(S)])

    V = np.zeros(A)
    theta = 0.001
    policy_stable = False
    # keep evaluating and improving until under delta threshold
    while not policy_stable:
        V = evaluation(theta, gamma, pi, V, P, R)
        policy_stable, pi = improvement(gamma, pi, V, P, R)
    
    return V, pi 


# -


