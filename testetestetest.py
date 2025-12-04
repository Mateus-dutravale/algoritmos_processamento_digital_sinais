from scipy import signal
import numpy as np
import matplotlib.pyplot as plt 
from funcoes import *

taps = 20  
fs = 10000
fc = 1000
wc =(np.pi*fc)/(fs/2)

b = signal.firwin(taps, fc, window= 'hamming', fs=fs)
w, h = signal.freqz(b)

mag_db = 20 * np.log10(np.maximum(np.abs(h), 1e-12))
mag_amp = np.abs(h)


plotagemRespostaFrequencia(w, mag_db, mag_amp, fc, 0)