import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.fft as scf
from . import plotagens as pl


# sinais de entrada
def inpulse(n):
    imp = []
    for element in n:
        if element == 0:
            imp.append(1)
        else:
            imp.append(0)
    return imp

def step(n):
    stp = []
    for element in n:
        if element >= 0:
            stp.append(1)
        else:
            stp.append(0)
    return stp

def ramp(n):
    rmp = []
    for element in n:
        if element >= 0:
            rmp.append(1 * element)  # Multiplicação mantida como no C++
        else:
            rmp.append(0)
    return rmp

def exponencial(n, a):
    exp = []
    for element in n:
        exp.append(math.pow(a, element))
    return exp

def cos(n, w0):
    return np.cos(n * (w0))

def sen(n, w0):
    return np.sin(n * (w0))

#  operações discretas
def atraso(n, d):   
    at = np.zeros(d)
    at = np.concatenate((at, n))
    at = at[:len(n)]
    return at
       
def adiantar(n, d):  
    ad = n[d:]
    ad = np.concatenate((ad, np.zeros(d)))
    return ad

def deslocamento(n, d):  
    if d > 0:
        return atraso(n, d)
    elif d < 0:
        return adiantar(n, -d)
    else:
        return n
    
def reflexao(n):
    return n[::-1]


def amostragemXN(xc, T): 
    xs = np.zeros(len(xc)) 
    for n in range(0, len(xc), T): 
        xs[n] = xc[n] 
    return xs

def sinalAmostrado(n, xc, T):
    N = len(n)

    xn = amostragemXN(xc, T)
    
    # FFTs normalizadas
    xtfft = scf.fftshift(scf.fft(xc, N)) / N
    xnfft = scf.fftshift(scf.fft(xn, N)) / N
    
    pl.plotagemQuatroGraficos(
        n, xc,        
        n, xn,  
        np.linspace(-np.pi, np.pi, N), np.abs(xtfft),  
        np.linspace(-np.pi, np.pi, N), np.abs(xnfft)
    )
    
    return xn 

def sinalReconstruido(n, xn, T):
    N = len(n)

    fs = 1/T
    wc = 2 * np.pi * (fs/2)      # banda máxima = fs/2
    
    omega = np.fft.fftshift(np.fft.fftfreq(N, d=1)) * 2*np.pi
    Hw = np.zeros(N)
    Hw[np.abs(omega) <= wc] = 1  # passa-baixa ideal
    
    pl.plotSignal(n, Hw, title="Filtro passa-baixa")
    
    # Reconstrução
    xnfft = scf.fftshift(scf.fft(xn, N)) / N
    Xrec = xnfft * Hw
    Xtrec = scf.ifft(scf.ifftshift(Xrec)) * T
    
    pl.plotSignal(n, np.real(Xtrec), title="Sinal reconstruído")
    
    return np.real(Xtrec)    
    


__all__ = ['inpulse', 'step', 'ramp', 'exponencial', 'cos', 'sen','atraso', 'adiantar', 'deslocamento', 'reflexao', 'amostragemXN', 'sinalAmostrado', 'sinalReconstruido']