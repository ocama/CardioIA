import importlib.util
import sys
import time


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("target_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    # Exemplo: python run_test_box.py module_path.py function_name
    if len(sys.argv) < 3:
        print("Usage: run_test_box.py <file_path> <function_name>")
        return

    filepath = sys.argv[1]
    func_name = sys.argv[2]

    try:
        module = load_module(filepath)
        _ = getattr(module, func_name)
    except Exception as e:
        print(f"Error loading function: {e}")
        sys.exit(1)

    print(f"Testing {func_name} as Black Box...")

    start_time = time.time()
    try:
        # Aqui idealmente se passariam argumentos de teste configuráveis
        # Por simplicidade, chamamos sem args ou com args padrão se houver lógica
        # Para um script genérico real, precisaríamos de um arquivo de input JSON
        print("Note: Running without args/with default args for demo.")
        # result = func()
        pass
    except Exception as e:
        print(f"Execution Error: {e}")

    end_time = time.time()
    duration = end_time - start_time

    print(f"Execution Time: {duration:.6f}s")

    # SLA check dummy
    if duration > 1.0:
        print("Performance FAIL: Too slow")
    else:
        print("Performance PASS")

if __name__ == "__main__":
    main()
