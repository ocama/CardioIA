import os

def generate_clinical_texts(output_dir="../assets"):
    os.makedirs(output_dir, exist_ok=True)
    
    text1 = """# REVISÃO CLÍNICA E ALORÍTMICA: DETECÇÃO DE ARRITMIAS VIA COMPUTAÇÃO NA BORDA (EDGE) NO PROJETO NAFIS

## Resumo
A implementação da telemetria de eletrocardiogramas (ECGs) em tempo real via Edge Computing representa um avanço vital na resposta clínica hospitalar. Este documento explora algoritmos determinísticos em oposição ao uso indiscriminado de Large Language Models (LLMs) para o diagnóstico vitalício, respeitando a diretriz "Math First, LLM Second" formulada no Projeto Nafis.

## Metodologia
Pacientes com suspeita de fibrilação atrial foram monitorados via dispositivos IoT (Protocolo MQTT). Os ensaios demonstraram que modelagens matemáticas para a extração do complexo QRS em hardwares limitados (Raspberry Pi/Microcontroladores Mikrotik) reduzem o atraso diagnóstico em 400% quando comparados ao processamento via Cloud centralizado. A GCP (Google Cloud Platform) é invocada secundariamente apenas para agregação populacional de Machine Learning e consolidação do Prontuário Eletrônico do Paciente.

## Conclusões
O emprego de análise estatística em sinais biológicos continua sendo o método mais eficaz e reprodutível na prevenção de falsos positivos cardiológicos em Unidades de Terapia Intensiva (UTI).

## Referências
- IBN AL-NAFIS. "O Comentário sobre a Anatomia no Cânon de Avicena", Circulação Pulmonar.
- SMITH, B., et al. "Edge computing for real-time cardiac monitoring". ArXiv, 2025.
"""

    text2 = """# LAUDO MÉDICO: CARDIOMIOPATIA HIPERTRÓFICA E AVALIAÇÃO DO RISCO CARDIOVASCULAR

**Paciente ID:** PID_0042
**Idade:** 68 anos
**Sexo:** Masculino
**Data da Avaliação:** 10 de Março de 2026

## Histórico Clínico
Paciente do sexo masculino, 68 anos, relata episódios de dispneia aos pequenos esforços e palpitações de início súbito nas últimas duas semanas. O histórico médico familiar indica morte súbita cardíaca em parente de primeiro grau (irmão, aos 55 anos). 

## Achados do Exame Físico
- Pressão Arterial: 145/90 mmHg.
- Frequência Cardíaca: 88 bpm (ritmo irregular).
- Ausculta Cardíaca: Sopro sistólico ejetivo grau III/VI audível no bordo esternal esquerdo, que exacerba com a manobra de Valsalva.

## Exames Complementares (Ecocardiograma / ECG)
A análise computacional primária da imagem do Ecocardiograma aponta:
- Espessura do septo interventricular: 19 mm (Normal: < 11 mm) evidenciando Hipertrofia Septal Assimétrica (HSA).
- Fração de Ejeção do Ventrículo Esquerdo (FEVE): 65% (Preservada).
- Eletrocardiograma numérico de Borda: Detectou extrassístoles ventriculares (ESV) frequentes nas 24h de monitoração do Holter digital.

## Plano de Ação e Processamento NLP
*Este laudo foi gerado e estruturado para que a arquitetura do "Doc Librarian" indexe suas entidades nomeadas (NER).* É recomendada a ablação septal caso a sintomatologia não responda aos beta-bloqueadores. Os dados deste laudo serão embutidos no dataset de Risco Cardiovascular via pipelines seguros e anonimizados, respeitando as normas da Lei Geral de Proteção de Dados Pessoais (LGPD).
"""

    path1 = os.path.join(output_dir, "artigo_edge_computing_nafis.md")
    path2 = os.path.join(output_dir, "laudo_clinico_pid_0042.md")
    
    with open(path1, "w", encoding="utf-8") as f:
        f.write(text1)
        
    with open(path2, "w", encoding="utf-8") as f:
        f.write(text2)
        
    print(f"Arquivos NLP gerados: \n - {path1}\n - {path2}")

if __name__ == "__main__":
    generate_clinical_texts()
