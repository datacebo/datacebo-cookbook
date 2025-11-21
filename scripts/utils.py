import subprocess
from pathlib import Path

def _get_modifed_notebooks(mode):
    """Returns a list of paths to modified notebooks.
    
    Args:
        mode (str): If `mode` is 'pr', then get the diff of changed notebooks between the PR branch
        and main. If it is 'commit', then get the diff of changed notebooks between the last two
        commits.
    """
    search = 'origin/main'if mode == 'pr' else 'HEAD~1 HEAD'
    git_diff = subprocess.run(
        ['git', 'diff', '--name-only', search, '--', '*.ipynb'],
        capture_output=True,
        text=True,
        check=True
    )
    notebook_paths = git_diff.stdout.splitlines()
    return [Path(line.strip()) for line in notebook_paths if line.strip()]
