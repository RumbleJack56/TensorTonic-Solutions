import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param = np.array(param,dtype=np.float64)
    grad = np.array(grad)
    m = np.array(m)
    v =  np.array(v)
    
    m_new = m * beta1 + (1-beta1)*grad
    v_new = v * beta2 + (1-beta2)*np.pow(grad,2)
    param -= lr / (1-beta1**t) * m_new / np.sqrt(v_new/(1-beta2**t)+eps)
    return param , m_new , v_new
    