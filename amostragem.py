import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift, fftfreq

###################################### Valores ########################################
f0 = 10.0     # Frequência 
fs = 3 * f0   # Frequência de amostragem > 2*f0 
Ts = 1.0 / fs # Período de amostragem
t_min = 0.0
t_max = 0.5   
N_fft = 8192  

###################################### Sinal contínuo #####################################
simFs = 100 * fs 
simTs = 1.0 / simFs
simT = np.arange(t_min, t_max, simTs) 
xc_t = np.cos(2 * np.pi * f0 * simT) #Mudar

######################################## amostragem #######################################
t_amostras = np.arange(t_min, t_max, Ts)
xn_valores = np.cos(2 * np.pi * f0 * t_amostras) #Mudar

######################################### trem de impulsos ################################
s_t = np.zeros_like(simT)
for t_n in t_amostras:
    idx = np.argmin(np.abs(simT - t_n))
    s_t[idx] = 1.0
xs_t = xc_t * s_t

#################################### reconstrução ##########################################
xr_t = np.zeros_like(simT) 
for i in range(len(xn_valores)):
    valor_amostra = xn_valores[i]
    tempo_amostra = t_amostras[i]
    sinc_deslocado = np.sinc((simT - tempo_amostra) / Ts)
    xr_t = xr_t + (valor_amostra * sinc_deslocado)

#################################### transformadas de fourier ##############################
freq_c = fftshift(fftfreq(N_fft, d=simTs))
Xc_fft_norm = fftshift(np.abs(fft(xc_t, N_fft))) / N_fft
Xs_fft_norm = fftshift(np.abs(fft(xs_t, N_fft))) / N_fft
Xr_fft_norm = fftshift(np.abs(fft(xr_t, N_fft))) / N_fft


####################################### gráfico #############################################
plt.figure(figsize=(14, 15)) 
plt.suptitle('Amostragem e Reconstrução')

#original
plt.subplot(3, 2, 1)
plt.plot(simT, xc_t, 'b', label=f'Sinal $x_c(t)$ (f0={f0} Hz)')
plt.title(f'1. Sinal Contínuo (f0 = {f0} Hz)')
plt.xlabel('Tempo (s)'); plt.ylabel('Amplitude')
plt.grid()
plt.xlim(t_min, t_max)

plt.subplot(3, 2, 2)
plt.plot(freq_c, Xc_fft_norm, 'b')
plt.title('2. Espectro Original |X_c(jω)|')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.xlim(-fs * 2, fs * 2)

#amostrado
plt.subplot(3, 2, 3)
plt.stem(t_amostras, xn_valores, 'g', basefmt=' ', linefmt='g-', markerfmt='go',label=f'Amostras $x[n]$ (Fs={fs}Hz)')
plt.title('3. Sinal Amostrado (Sequência $x[n]$)')
plt.xlabel('Tempo (s)'); plt.ylabel('Amplitude')
plt.grid()
plt.xlim(t_min, t_max)


plt.subplot(3, 2, 4)
plt.plot(freq_c, Xs_fft_norm, color='orange')
plt.title('4. Espectro Amostrado |X_s(jω)|')
plt.xlabel('Frequência (Hz)'); plt.ylabel('Magnitude')
plt.grid(True); plt.xlim(-fs * 2, fs * 2)
plt.annotate(f'Réplica (em fs = {fs} Hz)', xy=(fs, 0.02), xytext=(fs + 10, 0.05), arrowprops=dict(facecolor='black', shrink=0.05))

#reconstrução
plt.subplot(3, 2, 5)
plt.plot(simT, xc_t, 'b--', alpha=0.4)
plt.plot(simT, xr_t, 'r')
plt.plot(t_amostras, xn_valores, 'go', markersize=3)
plt.title('5. Sinal Reconstruído')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.xlim(t_min, t_max)

plt.subplot(3, 2, 6)
plt.plot(freq_c, Xr_fft_norm, 'r')
plt.title('6. Espectro Reconstruído |X_r(jω)|')
plt.xlabel('Frequência (Hz)'); plt.ylabel('Magnitude')
plt.grid()
plt.xlim(-fs * 2, fs * 2)

plt.subplots_adjust(top=0.94,bottom=0.07,left=0.1,right=0.95,hspace=0.5,wspace=0.3 )
plt.show()