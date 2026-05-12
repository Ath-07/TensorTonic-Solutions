def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here
    n_state = len(values)
    new_V = []

    for s in range(n_state):
        best = float('-inf')
        for a in range(len(transitions[0])):
            exp_future = 0
            for s_next in range(n_state):
                exp_future += (transitions[s][a][s_next] * values[s_next])
            q = rewards[s][a] +(gamma*exp_future)
            best = max(best, q)
        new_V.append(best)
    return new_V