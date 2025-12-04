import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from funcoes import *

fs = 10000 # Taxa de amostragem
fc = 1000  # Frequência de corte
M = 21 
N = M - 1  # Ordem do filtro (M=N+1)

wc_rad = 2 * np.pi * fc / fs 

hd_n = encontraHdn(N, wc_rad)
h_nc = aplicaJanelaRet(hd_n, N) 

b = h_nc 
# imprimeB(b)
a = [1.0]

# Calcula a resposta em frequência w (em Hz) e H (resposta complexa)
w, h = signal.freqz(b, a, worN=8192, fs=fs)
mag_db = 20 * np.log10(np.maximum(np.abs(h), 1e-12)) 
mag_amp = np.abs(h)

# Achar -3dB
idx_fc = np.argmin(np.abs(mag_db + 3))
fc_real = w[idx_fc]

# entradas para comparar
T_sinal = 0.01 
t = np.arange(0, T_sinal, 1/fs) 

# antes, proximo e depois da frequência de corte
freq1 = 600
freq2 = 1000 
freq3 = 2000

x1 = np.sin(2 * np.pi * freq1 * t) 
x2 = np.sin(2 * np.pi * freq2 * t) 
x3 = np.sin(2 * np.pi * freq3 * t)

y1 = filtroFIR(b, x1)
y2 = filtroFIR(b, x2)
y3 = filtroFIR(b, x3)

# plotagemTresGraficos(t, x1, x2, x3, y1, y2, y3, titulo1=f"Entrada {freq1} Hz", titulo2=f"Entrada {freq2} Hz", titulo3=f"Entrada {freq3} Hz")
plotagemRespostaFrequencia(w, mag_db, mag_amp, freq1, None)
# informacoes(T_sinal, freq1, freq2, freq3, x1,x2,x3,y1,y2,y3, N, M, wc_rad, fc_real)
