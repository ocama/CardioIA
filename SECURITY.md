# Política de Segurança — CardioIA

## Dados e Privacidade (LGPD / Lei 13.709/2018)

O CardioIA é um projeto **estritamente acadêmico** desenvolvido pela equipe na FIAP.

### Natureza dos Dados

| Dataset | Origem | Tipo | Status Privacidade |
|---|---|---|---|
| `uci_heart_disease_*.csv` | UCI ML Repository | Tabular, anônimo | ✅ Domínio Público |
| `ecg_paciente_*.png` | Gerado sinteticamente | Imagem sintética | ✅ Sem PII |
| `laudo_clinico_*.md` | Gerado para NLP | Dados fictícios | ✅ Não são pacientes reais |
| Artigos PubMed | NCBI / NLM | Texto científico aberto | ✅ Licença aberta |

> [!IMPORTANT]
> **Nenhum dado de paciente real é armazenado neste repositório.**
> Todos os dados clínicos são sintéticos ou provenientes de bases públicas anonimizadas.

### Comprometimentos LGPD

- ❌ Não coletamos dados pessoais identificáveis (PII)
- ❌ Não armazenamos prontuários reais
- ❌ Não processamos imagens de pacientes reais
- ✅ Dados de treino são de domínio público (UCI Heart Disease — Cleveland, 1988)
- ✅ Imagens ECG são geradas sinteticamente via `matplotlib`

---

## Reportando Vulnerabilidades

Se você encontrar uma vulnerabilidade de segurança neste repositório:

1. **NÃO abra uma issue pública** se a vulnerabilidade envolver exposição de dados sensíveis
2. Abra uma **Issue privada** (se disponível) ou envie um Pull Request com a correção
3. Use a label `security` em qualquer issue relacionada

### O que reportar

- Segredos ou credenciais hardcoded em código
- Dependências com CVEs conhecidos
- Endpoints ou URLs internas expostas
- Vazamento de dados de qualquer natureza

---

## Política para Fases Futuras (Fase 2 a 7)

À medida que o projeto evolui para APIs e modelos em produção:

- Toda chave de API deve usar **GitHub Secrets** ou variáveis de ambiente (`.env`)
- Modelos treinados com dados sensíveis **NÃO devem ser versionados** no repositório
- Endpoints de inferência devem implementar autenticação mínima (JWT ou API Key)
- Revisar este documento a cada nova Fase do PBL

---

## Referências

- [LGPD — Lei Geral de Proteção de Dados (Lei 13.709/2018)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [UCI Heart Disease Dataset — Licença](https://archive.ics.uci.edu/dataset/45/heart+disease)
- [NCBI / PubMed — Termos de Uso](https://www.ncbi.nlm.nih.gov/home/about/policies/)
