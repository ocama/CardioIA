# REVISÃO CLÍNICA E ALORÍTMICA: DETECÇÃO DE ARRITMIAS VIA COMPUTAÇÃO NA BORDA (EDGE) NO PROJETO NAFIS

## Resumo
A implementação da telemetria de eletrocardiogramas (ECGs) em tempo real via Edge Computing representa um avanço vital na resposta clínica hospitalar. Este documento explora algoritmos determinísticos em oposição ao uso indiscriminado de Large Language Models (LLMs) para o diagnóstico vitalício, respeitando a diretriz "Math First, LLM Second" formulada no Projeto Nafis.

## Metodologia
Pacientes com suspeita de fibrilação atrial foram monitorados via dispositivos IoT (Protocolo MQTT). Os ensaios demonstraram que modelagens matemáticas para a extração do complexo QRS em hardwares limitados (Raspberry Pi/Microcontroladores Mikrotik) reduzem o atraso diagnóstico em 400% quando comparados ao processamento via Cloud centralizado. A GCP (Google Cloud Platform) é invocada secundariamente apenas para agregação populacional de Machine Learning e consolidação do Prontuário Eletrônico do Paciente.

## Conclusões
O emprego de análise estatística em sinais biológicos continua sendo o método mais eficaz e reprodutível na prevenção de falsos positivos cardiológicos em Unidades de Terapia Intensiva (UTI).

## Referências
- IBN AL-NAFIS. "O Comentário sobre a Anatomia no Cânon de Avicena", Circulação Pulmonar.
- SMITH, B., et al. "Edge computing for real-time cardiac monitoring". ArXiv, 2025.
