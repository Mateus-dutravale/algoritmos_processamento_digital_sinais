import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from funcoes import *


# Parâmetros do filtro
fs = 10000      # amostragem
fp = 1000       # frequência de passagem
fs_stop = 2000  # frequência de rejeição
gpass = 1       # dB
gstop = 15      # dB

# b, a, N, Wn = criar_filtro(fs, fp, fs_stop, gpass, gstop)
N, Wn_analog = valores_filtro(fs, fp, fs_stop, 0.89125, 0.17783)
Wn_digital = 2 * np.arctan(Wn_analog / 2) / np.pi
b, a = signal.butter(N, Wn_digital, btype='low')

# Resposta em frequência
w, h = signal.freqz(b, a, worN=8192, fs=fs)
mag_db = 20 * np.log10(np.maximum(np.abs(h), 1e-12))
mag_amp = np.abs(h)

# entradas para comparar
T = 0.01
t = np.arange(0, T, 1/fs)

# w e mag_db já calculados antes
idx_fc = np.argmin(np.abs(mag_db + 3)) 
fc_real = w[idx_fc]

# print(f"w (Hz) = {w}\nFc = {fc_real:.2f} Hz")

# antes, proximo e depois da frequência de corte
x1 = np.sin(2*np.pi*500*t)
x2 = np.sin(2*np.pi*1000*t)
x3 = np.sin(2*np.pi*2000*t)

y1 = signal.lfilter(b, a, x1)
y2 = signal.lfilter(b, a, x2)
y3 = signal.lfilter(b, a, x3)

# plot da Entrada e saída, e sua variação conforme aproximação e passagem da frequencia de corte 
plotagemTresGraficos(t, x1, x2, x3, y1, y2, y3, titulo1="Entrada 500 Hz", titulo2="Entrada 1000 Hz", titulo3="Entrada 2000 Hz")
# plotagem da Resposta em frequência
plotagemRespostaFrequencia(w, mag_db, mag_amp, fp, fs_stop)

# tempo × frequência
print("Verificacao resposta temporal")
print(f"Entrada 500 Hz")
print(f"Saida RMS: {np.sqrt(np.mean(y1**2)):.4f}\n")

print(f"Entrada 1000 Hz")
print(f"Saida RMS: {np.sqrt(np.mean(y2**2)):.4f}\n")

print(f"Entrada 2000 Hz")
print(f"Saida RMS: {np.sqrt(np.mean(y3**2)):.4f}\n")
