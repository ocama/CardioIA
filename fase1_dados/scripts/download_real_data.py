import os
import json
import logging
import requests
import pandas as pd

# ------------------------------------------------------------------------------
# Governança de Scripts - MLOps (PEP-8 / Clean Code)
# ------------------------------------------------------------------------------
# Skills Ativadas:
# @ops_sre: Automação de logging para observabilidade e rastreabilidade da pipe.
# @doc_librarian: Padronização de ingestão e arquivamento dos arquivos mestres.
# ------------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Caminho absoluto baseado no local do script para garantir integridade (Clean Code)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(BASE_DIR, '..', 'datasets')
ASSETS_DIR = os.path.join(BASE_DIR, '..', 'assets')

def download_uci_heart_disease() -> None:
    """
    Ingesta o dataset UCI Heart Disease (Real).
    Regras aplicadas por:
    - @iot_engineer: Captura fidedigna das telemetrias na ponta (UCI).
    - @val_validator: Garantia de higienização de nulos na fonte primária.
    """
    os.makedirs(DATASETS_DIR, exist_ok=True)
    logging.info("Buscando dados Tabulares reais da UCI Repository...")
    
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
    columns = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", 
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]
    
    try:
        df = pd.read_csv(url, names=columns, na_values="?")
        # Validação Básica de Qualidade (@val_validator)
        df = df.dropna()
        output_path = os.path.join(DATASETS_DIR, "uci_heart_disease_real.csv")
        df.to_csv(output_path, index=False)
        logging.info(f"[OK] Dataset UCI salvo: {output_path} ({len(df)} linhas limpas).")
    except Exception as e:
        logging.error(f"Erro ao baixar UCI: {e}")

def fetch_medical_texts() -> None:
    """
    Raspa literatura aberta global para NLP.
    Regras aplicadas por:
    - @pol_polyglot: Garantia de extração do idioma fonte correto para futura modelagem.
    """
    os.makedirs(ASSETS_DIR, exist_ok=True)
    logging.info("Buscando dados Textuais reais e abertos (Wikipedia API)...")
    
    topics = {
        "Cardiologia": "https://pt.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cardiologia&format=json",
        "Eletrocardiograma": "https://pt.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Eletrocardiograma&format=json"
    }
    
    headers = {"User-Agent": "Projeto_CardioIA_Academico/1.0 (omar.assem@example.com)"}
    
    for title, url in topics.items():
        try:
            resp = requests.get(url, headers=headers)
            data = resp.json()
            pages = data.get('query', {}).get('pages', {})
            
            # Pega o primeiro ID de pagina do dict
            page_id = list(pages.keys())[0]
            text = pages[page_id].get('extract', '')
            
            if text:
                output_path = os.path.join(ASSETS_DIR, f"{title.lower()}_real_text.txt")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(f"FONTE: WIKIPEDIA (CONTEUDO LIVRE)\n\n{text}")
                logging.info(f"[OK] Texto '{title}' extraído com sucesso.")
            else:
                logging.warning(f"Texto vazio para '{title}'.")
                
        except Exception as e:
            logging.error(f"Erro ao extrair texto de {title}: {e}")

if __name__ == "__main__":
    download_uci_heart_disease()
    fetch_medical_texts()
