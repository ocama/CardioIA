#!/bin/bash
#
# Script: Engineering Excellence Quality Gate
# Descrição:
#   Orquestra a pipeline de validação contínua (CI/CD Local).
#   Executa Linting (Ruff), Tipagem Estática (Mypy), Testes Unitários (Pytest)
#   e Verificação de Segurança (Ruff-Sec).
# Uso:
#   ./eng_excellence.sh
#

set -e # Aborta se qualquer comando falhar

echo "🚀 [VAL] Iniciando Engenharia de Excelência..."

# 1. Linting & Complexity (Ruff)
echo "🔍 [1/4] Rodando Ruff (Linting & Complexidade)..."
ruff check .

# 2. Typing (Mypy)
echo "📏 [2/4] Rodando Mypy (Static Typing)..."
mypy . --ignore-missing-imports

# 3. Unit Tests & Coverage (Pytest)
echo "🧪 [3/4] Rodando Pytest & Coverage..."
pytest --cov=. --cov-report=term-missing --cov-fail-under=90 tests/

# 4. Security (Ruff Security Rules)
echo "🛡️ [4/4] Verificando Vulnerabilidades (Ruff S-Rules)..."
ruff check . --select=S

echo "✅ [VAL] Todos os critérios de Engenharia de Excelência foram atingidos!"
