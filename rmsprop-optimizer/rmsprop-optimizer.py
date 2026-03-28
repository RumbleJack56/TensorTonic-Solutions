import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    w , g , s = np.array(w, dtype=np.float64) , np.array(g) , np.array(s)
    s = beta * s + (1 - beta) * np.pow(g,2)
    w -=  lr * (g * np.pow(s+eps,-0.5))
    return w, s