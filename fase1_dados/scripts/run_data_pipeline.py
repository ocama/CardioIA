import os
import json
import logging
import pandas as pd

# ------------------------------------------------------------------------------
# MLOps Pipeline de Dados - Atuação das Skills CardioIA
# ------------------------------------------------------------------------------
# Este roteiro materializa o papel de cada agente/skill no tratamento de Big Data Médica.
# ------------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(name)s] - %(message)s')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(BASE_DIR, '..', 'datasets')
ASSETS_DIR = os.path.join(BASE_DIR, '..', 'assets')

def skill_law_compliance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agentes: @law_compliance & @sec_guardian
    Missão: Garantir anonimização e conformidade ética (LGPD/GDPR/HIPAA).
    """
    logger = logging.getLogger("sec_guardian")
    logger.info("Iniciando auditoria de conformidade (Zero Trust)...")
    
    # Simula a anonimização de colunas sensíveis (PII)
    sensitive_cols = ['name', 'ssn', 'cpf', 'address', 'patient_id']
    dropped = [col for col in sensitive_cols if col in df.columns]
    
    if dropped:
        df = df.drop(columns=dropped)
        logger.info(f"Colunas sensíveis removidas pela LGPD: {dropped}")
    else:
        logger.info("Nenhuma coluna PII identificada. Dataset previamente anonimizado na origem.")
        
    return df

def skill_val_validator(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agente: @val_validator & @opt_optimizer
    Missão: MLOps QA e validação estatística de ranges vitais.
    """
    logger = logging.getLogger("val_validator")
    logger.info("Iniciando validação de Qualidade dos tensores (Ranges e Zeros)...")
    
    inicial_len = len(df)
    # Validação Básica da Homeostase (Idade > 0, Colesterol coerente)
    if 'age' in df.columns:
        df = df[(df['age'] > 0) & (df['age'] < 120)]
        
    if 'chol' in df.columns:
        df = df[df['chol'] > 50] # Um valor impossível (abaixo de 50mg/dL de colesterol rebaixaria à morte subita)
        
    removidas = inicial_len - len(df)
    logger.info(f"Qualidade Atendida: {removidas} linhas estatisticamente inconsistentes removidas do dataset vital.")
    return df

def skill_doc_librarian(df: pd.DataFrame, output_name: str) -> None:
    """
    Agente: @doc_librarian & @knowledge_protocol
    Missão: Curadoria de metadados, indexação e criação do dicionário de dados (Data Dictionary).
    """
    logger = logging.getLogger("doc_librarian")
    logger.info("Catalogando metadados acadêmicos para Dicionário de Dados JSON...")
    
    data_dict = {
        "dataset_name": output_name,
        "schemas": {col: str(df[col].dtype) for col in df.columns},
        "total_rows": len(df),
        "mean_age": float(df['age'].mean()) if 'age' in df.columns else None,
        "features_coronarianas": ["chol", "trestbps", "cp", "restecg"],
        "categorical_mapping": {
            "sex": {"1": "Masculino", "0": "Feminino"},
            "cp (Chest Pain Type)": {"1": "Angina Típica", "2": "Angina Atípica", "3": "Dor não-anginosa", "4": "Assintomático"},
            "fbs (Fasting Blood Sugar)": {"1": "> 120 mg/dl", "0": "<= 120 mg/dl"},
            "target": {"0": "Sem Doença", "1-4": "Presença de Doença Cardíaca (níveis de severidade)"}
        }
    }
    
    dict_path = os.path.join(ASSETS_DIR, f"{output_name}_metadata.json")
    with open(dict_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=4)
        
    logger.info(f"Metadados estruturados e indexados em: {dict_path}")

def main():
    logger = logging.getLogger("orq_orchestrator")
    logger.info("Iniciando Orquestração do Pipeline Central de Dados (DAG Simulada)...")
    
    uci_path = os.path.join(DATASETS_DIR, "uci_heart_disease_real.csv")
    if not os.path.exists(uci_path):
        logger.error(f"Dataset primordial não encontrado em {uci_path}. Execute o crawler antes.")
        return
        
    df = pd.read_csv(uci_path)
    logger.info(f"Dataset bruto carregado. Shape inicial: {df.shape}")
    
    # 1. Atuação Ética (@law_compliance)
    df = skill_law_compliance(df)
    
    # 2. Atuação Estatística e Clínica (@val_validator)
    df = skill_val_validator(df)
    
    # 3. Catalogação de Metainformação Acadêmica (@doc_librarian)
    skill_doc_librarian(df, "uci_heart_disease")
    
    # Salvando a versão ouro validada
    final_path = os.path.join(DATASETS_DIR, "uci_heart_disease_ouro.csv")
    df.to_csv(final_path, index=False)
    logger.info(f"Pipeline concluído. Dataset versão-ouro exportado (Shape final: {df.shape}).")

if __name__ == "__main__":
    main()
