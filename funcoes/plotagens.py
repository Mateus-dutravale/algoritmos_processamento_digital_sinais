import matplotlib.pyplot as plt
import numpy as np

def plotSignal(n, x, title="Sinal"):
    plt.plot(n, x)
    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("amplitude")
    plt.grid()
    plt.show()

def plotagemDoisGraficos(n, x, y, title1="Sinal 1", title2="Sinal 2"):
    fig, (ax1, ax2) = plt.subplots(2,sharex=True, figsize=(10,6))
    
    ax1.stem(n, x)
    ax1.set_title(title1)
    ax1.set_xlabel("n")
    ax1.set_ylabel("amplitude")
    ax1.grid()

    ax2.stem(n, y)
    ax2.set_title(title2)
    ax2.set_xlabel("n")
    ax2.set_ylabel("amplitude")
    ax2.grid()

    plt.tight_layout()
    plt.show()
    
def plotagemQuatroGraficos(t1, x1, t2, x2, f1, X1, f2, X2,
                           titulo1="Sinal x(t)", titulo2="Sinal x[n]",
                           titulo3="FFT x(t)", titulo4="FFT x[n]"):

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(10,8), sharex=False)

    ax1.plot(t1, x1)
    ax1.set_title(titulo1)
    ax1.grid()

    ax2.plot(t2, x2)
    ax2.set_title(titulo2)
    ax2.grid()

    ax3.stem(f1, X1)
    ax3.set_title(titulo3)
    ax3.grid()

    ax4.stem(f2, X2)
    ax4.set_title(titulo4)
    ax4.grid()

    plt.tight_layout()
    plt.show()
    
def plotagemTresGraficos(t, x1, x2, x3, y1, y2, y3,
                           titulo1="Sinal 1", titulo2="Sinal 2", titulo3="Sinal 3"):
    plt.figure(figsize=(14,8))
    plt.subplot(3,1,1)
    plt.plot(t, x1, label=titulo1)
    plt.plot(t, y1, label='Saída filtrada')
    plt.title('Comparação Entrada × Saída — Frequência 500 Hz (antes do corte)')
    plt.grid(); plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t, x2, label=titulo2)
    plt.plot(t, y2, label='Saída filtrada')
    plt.title('Comparação Entrada × Saída — Frequência 1000 Hz (próxima ao corte)')
    plt.grid()
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t, x3, label=titulo3)
    plt.plot(t, y3, label='Saída filtrada')
    plt.title('Comparação Entrada × Saída — Frequência 2000 Hz (acima do corte)')
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()
        
        
def plotagemRespostaFrequencia(w, mag_db, mag_amp, fc, fs_stop):
    if (fs_stop == None):
        plt.figure(figsize=(12,5))

        plt.subplot(1,2,1)
        plt.plot(w, mag_db)
        plt.axvline(fc, color='C1', linestyle='--', label=f'fp = {fc} Hz')
        # plt.axvline(fs_stop, color='C2', linestyle='--', label=f'fs_stop = {fs_stop} Hz')
        plt.title('Resposta em Magnitude (dB)')
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Magnitude (dB)')
        plt.grid(True)
        plt.ylim([-80, 5])
        plt.xlim
        plt.legend()

        plt.subplot(1,2,2)
        plt.plot(w, mag_amp)
        plt.axvline(fc, color='C1', linestyle='--')
        # plt.axvline(fs_stop, color='C2', linestyle='--')
        plt.title('Amplitude / Ganho (Linear)')
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Amplitude')
        plt.grid(True)

        plt.tight_layout()
        plt.show()
    else:
        plt.figure(figsize=(12,5))

        plt.subplot(1,2,1)
        plt.plot(w, mag_db)
        plt.axvline(fc, color='C1', linestyle='--', label=f'fp = {fc} Hz')
        plt.title('Resposta em Magnitude (dB)')
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Magnitude (dB)')
        plt.grid(True)
        plt.ylim([-80, 5])
        plt.xlim
        plt.legend()

        plt.subplot(1,2,2)
        plt.plot(w, mag_amp)
        plt.axvline(fc, color='C1', linestyle='--')
        plt.title('Amplitude / Ganho (Linear)')
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Amplitude')
        plt.grid(True)

        plt.tight_layout()
        plt.show()
    
    
def informacoes (freq1, freq2, freq3, x1, y1, y2, y3, N, M, wc_rad, fc_real):
    print("\n--- Verificacao da Resposta e algumas informacoes ---")

    print(f"Ordem filtro (N): {N}")
    print(f"Numero de Coeficientes (M): {M}")
    print(f"Frequencia de Corte (wc_rad): {wc_rad:.4f} rad/amostra")
    print(f"Frequencia de corte(-3dB): {fc_real:.2f} Hz")

    # Cálculo e impressão do valor RMS da saída
    rms_in_ideal = np.sqrt(np.mean(x1**2))
    print(f"RMS da Entrada (Ideal): {rms_in_ideal:.4f}")

    print(f"\nEntrada {freq1} Hz (Passagem)")
    print(f"Saida RMS: {np.sqrt(np.mean(y1**2)):.4f}")

    print(f"\nEntrada {freq2} Hz (Transicao)")
    print(f"Saida RMS: {np.sqrt(np.mean(y2**2)):.4f}")

    print(f"\nEntrada {freq3} Hz (Rejeicao)")
    print(f"Saida RMS: {np.sqrt(np.mean(y3**2)):.4f}")
    
def imprimeB(b):
    for x in b:
        print(f'{x},')
       
__all__ = ['plotSignal', 'plotagemDoisGraficos', 'plotagemQuatroGraficos', 'plotagemTresGraficos', 'plotagemRespostaFrequencia', 'informacoes', 'imprimeB']