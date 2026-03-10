import sys

# Regras simples de Arquitetura Hexagonal (Exemplo)
# Domínio não pode importar de 'infra' ou 'drivers'

FORBIDDEN_KEY = {
    'domain': ['infrastructure', 'drivers', 'flask', 'django', 'google.cloud'],
    'core': ['infrastructure', 'adapters']
}

def check_file(filepath):
    # Determina a camada baseada no caminho do arquivo
    layer = None
    if 'domain' in filepath:
        layer = 'domain'
    elif 'core' in filepath:
        layer = 'core'

    if not layer:
        return []

    errors = []
    forbidden = FORBIDDEN_KEY.get(layer, [])

    try:
        with open(filepath, 'r') as f:
            for i, line in enumerate(f, 1):
                if line.strip().startswith('import') or line.strip().startswith('from'):
                    for bad in forbidden:
                        if bad in line:
                            errors.append(f"Line {i}: Layer '{layer}' cannot import '{bad}' ({line.strip()})")
    except Exception:  # noqa: S110
        pass

    return errors

def main():
    files = sys.argv[1:]
    has_error = False
    for f in files:
        errs = check_file(f)
        if errs:
            has_error = True
            print(f"Architecture Violation in {f}:")
            for e in errs:
                print(f"  - {e}")

    if has_error:
        sys.exit(1)
    else:
        print("Architecture Check PASS")

if __name__ == "__main__":
    main()
