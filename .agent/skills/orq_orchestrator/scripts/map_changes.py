import json
import os
import subprocess


def get_git_diff():
    try:
        # Get list of changed files relative to main/master or just currently modified
        result = subprocess.run(['/usr/bin/git', 'diff', '--name-only'], capture_output=True, text=True)
        return result.stdout.splitlines()
    except Exception:
        return []

def get_dir_structure(root='.'):
    structure = {}
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        structure[dirpath] = filenames
    return structure

def main():
    changes = get_git_diff()
    # structure = get_dir_structure() # Commented out to save tokens, only enabling if requested

    print(json.dumps({
        "changed_files": changes,
        "note": "Use 'git diff' output to decide which agents to dispatch."
    }, indent=2))

if __name__ == "__main__":
    main()
