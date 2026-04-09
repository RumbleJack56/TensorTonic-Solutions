import numpy as np
def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    values , transitions , rewards = np.array(values) , np.array(transitions) , np.array(rewards)
    return ((transitions * values[None,:]).sum(axis=-1)*gamma + rewards).max(axis=-1).tolist()