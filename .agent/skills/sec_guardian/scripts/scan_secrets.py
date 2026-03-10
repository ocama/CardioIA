import re
import sys

# Padrões simples de regex para segredos comuns
PATTERNS = {
    'AWS_KEY': r'AKIA[0-9A-Z]{16}',
    'PRIVATE_KEY': r'-----BEGIN PRIVATE KEY-----',
    'GENERIC_TOKEN': r'(api_key|access_token|secret)\s*[:=]\s*["\'][a-zA-Z0-9-_\.]+["\']',
    'IPV4_ADDRESS': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
}

def scan_file(filepath):
    found_issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_no, line in enumerate(f, 1):
                for key, pattern in PATTERNS.items():
                    if re.search(pattern, line):
                        # Ignora placeholders comuns
                        if "EXAMPLE" in line or "YOUR_" in line:
                            continue
                        found_issues.append(f"{key} found at line {line_no}")
    except Exception as e:
        return [f"Error reading file: {str(e)}"]

    return found_issues

def main():
    files = sys.argv[1:]
    if not files:
        # Se nenhum arquivo passado, tenta ler do git diff (simulado aqui ou passado via args)
        print("No files provided for scan.")
        return

    all_issues = {}
    for f in files:
        issues = scan_file(f)
        if issues:
            all_issues[f] = issues

    if all_issues:
        print("FAIL: Segredos potenciais encontrados.")
        for f, issues in all_issues.items():
            print(f"{f}: {issues}")
        sys.exit(1)
    else:
        print("PASS: Nenhum segredo óbvio encontrado.")
        sys.exit(0)

if __name__ == "__main__":
    main()
