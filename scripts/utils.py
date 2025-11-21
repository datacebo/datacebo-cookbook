import subprocess
from pathlib import Path

def _get_modifed_notebooks(mode):
    """Returns a list of paths to modified notebooks.
    
    Args:
        mode (str): If `mode` is 'pr', then get the diff of changed notebooks between the PR branch
        and main. If it is 'commit', then get the diff of changed notebooks between the last two
        commits.
    """
    process_args = ['git', 'diff', '--name-only']
    if mode == 'pr':
        process_args.append('origin/main')
    elif mode == 'commit':
        process_args.extend(['HEAD~1', 'HEAD'])
    else:
        raise ValueError("'mode' must be either 'commit' or 'pr'")
    
    process_args.extend(['--', '*.ipynb'])
    git_diff = subprocess.run(
        process_args,
        capture_output=True,
        text=True,
        check=True
    )
    notebook_paths = git_diff.stdout.splitlines()
    return [Path(line.strip()) for line in notebook_paths if line.strip()]
