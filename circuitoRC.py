import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode


def capacitancia(r, fc):
    cap = 1/(2*np.pi*r*fc)
    return cap


R = 220          # ohms
C = 33e-6      # farads
tau = R * C
fc = 1/(2*np.pi*tau)

# Função de transferência H(s) = 1 / (RCs + 1)
num = [1]
den = [tau, 1]
system = TransferFunction(num, den)

w, mag, phase = bode(system)   
freq = w / (2*np.pi)

A = 1           # Amplitude
f0 = 100         # Frequência sinal
fase = np.deg2rad(45)  # fase de entrada em radianos
t_final = 1          
fa = 2000            # taxa de amostragem 
t = np.linspace(0, t_final, int(fa*t_final), endpoint=False)

Vin = A * np.sin(2*np.pi*f0*t + fase)

idx = np.argmin(np.abs(freq - f0))

H_abs = 10**(mag[idx]/20)           # Converte magnitude de dB 
H_fase = np.deg2rad(phase[idx])    # Converte fase para radianos

Vout = H_abs * A * np.sin(2*np.pi*f0*t + fase + H_fase)

print(f"Frequencia de corte: {fc:.4f} Hz")
print(f"Para f0 = {f0:.4f} Hz:")
print(f"H(jw) = {H_abs:.4f}")
print(f"Fase do filtro = {np.rad2deg(H_fase):.4f} graus\n")

# ------------------ PLOTS ------------------
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
ganho = 10**(mag/20)  # conversão de dB para ganho
plt.semilogx(freq, ganho)
plt.axvline(fc, color='r', linestyle='--', label=f'fc = {fc:.3f} Hz')
plt.title("Bode - Amplitude")
plt.ylabel("Ganho (|H(jω)|)")
plt.grid(True, which="both")
plt.legend()


plt.subplot(3,1,2)
plt.semilogx(freq, phase)
plt.axvline(fc, color='r', linestyle='--', label=f'fc = {fc:.3f} Hz')
plt.title("Bode - Fase")
plt.ylabel("Fase (graus)")
plt.grid(True, which="both")
plt.legend()

plt.subplot(3,1,3)
plt.plot(t, Vin, label="Entrada Vin(t)")
plt.plot(t, Vout, label="Saída Vout(t) - Teórica", linewidth=2)
plt.title("Comparação no Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
# cap = capacitancia(R, fc)
# print(cap)