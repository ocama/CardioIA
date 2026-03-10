import os
import sys


def count_tokens_approx(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Estimativa grosseira: 1 token ~= 4 caracteres
            return len(content) / 4
    except Exception:
        return 0

def main():
    files = sys.argv[1:]
    total_tokens = 0
    for f in files:
        if os.path.exists(f):
            total_tokens += count_tokens_approx(f)

    # Custo aproximado Gemini 1.5 Pro (check pricing)
    # Exemplo figurativo: $7.00 per 1M input tokens
    cost = (total_tokens / 1_000_000) * 7.00

    print(f"Estimated Tokens: {int(total_tokens)}")
    print(f"Estimated Input Cost (USD): ${cost:.4f}")

    if total_tokens > 100000:
        print("WARNING: Contexto excede 100k tokens. Considere processar em chunks.")

if __name__ == "__main__":
    main()
