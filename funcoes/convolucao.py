import numpy as np
import matplotlib.pyplot as plt
import math


def conv(x, h):
    # o vetor h é a resposta ao impulso
    N = len(x)
    M = len(h)
    len_y = N + M - 1
    y = np.zeros(len_y)
    
    for n in range(len_y):
        soma = 0
        for k in range(N):
            if 0 <= n - k < M:
                soma += x[k] * h[n - k]
        y[n] = soma
        
    return y

def filtroFIR(b, x):
    return np.convolve(b,x, mode = 'same')


__all__ = ['conv', 'filtroFIR']
