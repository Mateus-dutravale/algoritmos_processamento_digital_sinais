import numpy as np
import math
from . import plotagens as pl

def eqSegundoGrau(y2,y1,y0):
    delta = (y1**2) - 4*y2*y0
    if delta > 0:
        r1 = (-y1 - math.sqrt(delta))/ (2*y2)
        r2 = (-y1 + math.sqrt(delta)) / (2*y2)
        raizes = np.array([r1, r2])
        matriz_AX = np.array([[r1**-1, r2**-1],[r1**-2, r2**-2]])
    return matriz_AX, raizes
                    #c1r1^-1 + c2r2^-1 = cond1
                    #c1r1^-2 + c2r2^-2 = cond2

def edohomogeneaNula(n,y2, y1, y0, cond1, cond2):
    A, raizes = eqSegundoGrau(y2, y1, y0)
    B = np.array([cond1, cond2])
    X = np.linalg.solve(A, B)
    
    
    solucao = []
    for element in n:
        result = X[0]*np.power(raizes[0], element) + X[1]*np.power(raizes[1], element)
        solucao.append(result)
    
    pl.plotSignal(n, solucao, title="Solução da EDO homogênea com resposta a entrada nula")
    
    print("y(n) = {}*{}^n + {}*{}^n".format(X[0],raizes[0], X[1], raizes[1]))
    return X


__all__ = ['eqSegundoGrau', 'edohomogeneaNula']
    