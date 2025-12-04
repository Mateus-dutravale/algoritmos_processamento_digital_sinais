import sympy as sp
import math
import numpy as np

def fraParciais(num, den):
    z = sp.symbols('z')
    y = sp.factor(num/den)
    f = sp.apart(y)
    
    sp.pprint(f)
    return f


def medMovel(x, M):
    y = []
    for i in range(len(x)):
        soma = 0
        cont = 0
        for j in range(M):
            if i - j >= 0:
                soma += x[i - j]     
                cont += 1            
        media = soma / cont         
        y.append(media)            
    return np.array(y)


__all__ = ['fraParciais', 'medMovel']

