import os
import matplotlib.pyplot as plt
import numpy as np

def simulate_ecg_signal(t, hear_rate=75, noise_level=0.05):
    """Gera um sinal sintético de ECG (Math First)."""
    # Converter batimentos por minuto em frequência (Hz)
    f = hear_rate / 60.0
    
    # O sinal ECG pode ser aproximado por uma soma de gaussianas e funções senoidais
    # P wave
    p_wave = 0.15 * np.sin(2 * np.pi * f * t) * np.exp(-((t % (1/f) - 0.2* (1/f))**2) / 0.005)
    # QRS complex
    qrs_wave = np.sin(2 * np.pi * f * t) * np.exp(-((t % (1/f) - 0.4* (1/f))**2) / 0.001)
    # T wave
    t_wave = 0.25 * np.sin(2 * np.pi * f * t) * np.exp(-((t % (1/f) - 0.7* (1/f))**2) / 0.01)
    
    signal = p_wave + qrs_wave + t_wave
    
    # Adicionando ruído (telemetria de borda real raramente é perfeita)
    noise = np.random.normal(0, noise_level, len(t))
    return signal + noise

def generate_ecg_images(num_images=105, output_dir="../images"):
    os.makedirs(output_dir, exist_ok=True)
    
    np.random.seed(100)
    
    t = np.linspace(0, 3, 1000) # 3 segundos de leitura
    
    print(f"Gerando {num_images} imagens de ECG...")
    for i in range(1, num_images + 1):
        hr = np.random.randint(50, 110)
        noise = np.random.uniform(0.01, 0.08)
        
        signal = simulate_ecg_signal(t, hear_rate=hr, noise_level=noise)
        
        plt.figure(figsize=(10, 4))
        plt.plot(t, signal, color='blue', linewidth=1)
        plt.title(f"Eletrocardiograma - Paciente {i:04d} (Simulação Math First)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Voltagem (mV)")
        plt.grid(True, linestyle='--', alpha=0.6)
        
        # Simular anomalias grosseiras se o heart rate for crítico
        if hr > 100:
            plt.axvspan(1.0, 1.5, color='red', alpha=0.3, label='Alerta: Taquicardia')
            plt.legend()
            
        plt.tight_layout()
        output_path = os.path.join(output_dir, f"ecg_paciente_{i:04d}.png")
        plt.savefig(output_path, dpi=150)
        plt.close()
        
    print(f"Imagens geradas em: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    generate_ecg_images()
