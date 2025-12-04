import numpy as np

def contaBancaria(y0, r, x, n):
    # não esqueça que x é uma lista a depender do numero de meses!!!!!
    soma = 0
    
    for k in range(n):
        soma += ((1 + r) ** (n - 1 - k)) * x[k]
        y_n = ((1 + r) ** n) * y0 + soma
    return y_n


__all__ = ['contaBancaria']
