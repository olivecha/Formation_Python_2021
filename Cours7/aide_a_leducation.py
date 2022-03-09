import numpy as np
import matplotlib.pyplot as plt

__all__ = ['tracer', 'np']

def tracer_plan_cartesien():
    plt.arrow(-1, 0, 2, 0, width=0.005, head_width=0.05, color='k')
    plt.arrow(0, -1, 0, 2, width=0.005, head_width=0.05, color='k')
    plt.grid('on')

def tracer(x, y, **kwargs):
    tracer_plan_cartesien()
    plt.plot(x, y, **kwargs)
    plt.legend()
    
def moyenne(x):
    return np.mean(x)