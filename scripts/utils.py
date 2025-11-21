import subprocess
from pathlib import Path

def _get_modifed_notebooks():
    """Returns a list of paths to modified notebooks.
    
    Returns:
        List of strings that represent paths to notebooks.
    """
    process_args = ['git', 'diff', '--name-only', 'origin/main', '--', '*.ipynb']
    git_diff = subprocess.run(
        process_args,
        capture_output=True,
        text=True,
        check=True
    )
    notebook_paths = git_diff.stdout.splitlines()
    return [line.strip() for line in notebook_paths if line.strip()]
