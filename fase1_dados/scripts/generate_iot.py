import pandas as pd
import numpy as np
import os

def generate_iot_dataset(num_samples=150, output_dir="../datasets"):
    os.makedirs(output_dir, exist_ok=True)
    
    np.random.seed(42)
    
    # Gerando dados baseados em distribuições realistas
    idade = np.random.normal(loc=60, scale=12, size=num_samples).astype(int)
    idade = np.clip(idade, 30, 95)
    
    sexo = np.random.choice(["Masculino", "Feminino"], size=num_samples, p=[0.55, 0.45])
    
    # Fatores correlacionados
    pressao_sistolica = np.random.normal(loc=120 + (idade - 50)*0.5, scale=15, size=num_samples).astype(int)
    pressao_diastolica = pressao_sistolica * 0.65 + np.random.normal(loc=0, scale=5, size=num_samples)
    pressao_diastolica = pressao_diastolica.astype(int)
    
    colesterol_ldl = np.random.normal(loc=110 + (idade - 40)*0.3, scale=25, size=num_samples).astype(int)
    
    frequencia_cardiaca = np.random.normal(loc=75, scale=12, size=num_samples).astype(int)
    
    # Geração de uma variável target (Risco Cardiovascular)
    risco_score = (
        (idade / 100) * 0.3 + 
        (pressao_sistolica / 200) * 0.4 + 
        (colesterol_ldl / 250) * 0.3
    )
    
    # Introduzir ruído
    risco_score += np.random.normal(0, 0.05, num_samples)
    
    risco_cardiovascular = np.where(risco_score > 0.65, "Alto", 
                                    np.where(risco_score > 0.45, "Medio", "Baixo"))
    
    df = pd.DataFrame({
        "Paciente_ID": [f"PID_{str(i).zfill(4)}" for i in range(1, num_samples+1)],
        "Idade": idade,
        "Sexo": sexo,
        "Pressao_Sistolica": pressao_sistolica,
        "Pressao_Diastolica": pressao_diastolica,
        "Colesterol_LDL": colesterol_ldl,
        "Frequencia_Cardiaca": frequencia_cardiaca,
        "Risco_Cardiovascular": risco_cardiovascular
    })
    
    output_path = os.path.join(output_dir, "telemetria_iot_cardio.csv")
    df.to_csv(output_path, index=False)
    print(f"Dataset de telemetria gerado com sucesso: {output_path} ({num_samples} linhas)")

if __name__ == "__main__":
    generate_iot_dataset()
