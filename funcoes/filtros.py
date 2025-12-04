import scipy.signal as signal
from sympy import symbols
from scipy.optimize import fsolve
import numpy as np
import math


def criar_filtro(fs, fp, fs_stop, gpass, gstop):
    #filtro Butterworth com parâmetros configuráveis
    wp = fp / (fs/2)
    ws = fs_stop / (fs/2)

    N, Wn = signal.buttord(wp, ws, gpass, gstop)
    b, a = signal.butter(N, Wn, btype='low')

    return b,a,N,Wn

def valores_filtro(fs, fp, fs_stop, h_amp1, h_amp2):
    wp = (2*np.pi*fp)/fs
    ws = (2*np.pi*fs_stop)/fs
    
    A = ((1/h_amp1)**2) -1
    B = (1/h_amp2)**2 -1
    
    # depois da dedução matematica...
    N = np.log(A/B)/(2*np.log(wp/ws))
    N = round(N) 
    
    # Aplicando N para obter Wn
    
    Wn = (wp)/((A)**(1/(2*N)))
    w = (wp)/(((1/h_amp1)**2) -1)**(1/(2*N))

    print(f'valor de N: {N}; valor de Wn: {Wn}')
    
    return N, Wn
    
def encontraHdn(N, wc_norm):
    M = N + 1
    
    # Vetor de tempo n, centrado em n=0 para um filtro não causal 
    n = np.arange(M) - N // 2
    
    wc_norm_pi = wc_norm / np.pi 
    hd = wc_norm_pi * np.sinc(wc_norm_pi * n)
    
    return hd

def aplicaJanelaRet(hd, N):
    
    janela_retangular = np.ones(N + 1)
    hw = hd * janela_retangular
    
    return hw



__all__ = ['criar_filtro', 'valores_filtro', 'encontraHdn', 'aplicaJanelaRet']