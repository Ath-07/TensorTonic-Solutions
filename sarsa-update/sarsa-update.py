def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    # Write code here
    TD = reward + gamma * q_table[next_state][next_action] - q_table[state][action]
    Q_table_copy = []
    for i in range(len(q_table)):
        Q_table_copy.append(q_table[i])
    Q_table_copy[state][action] += alpha * TD
    return Q_table_copy