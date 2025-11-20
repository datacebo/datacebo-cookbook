import argparse
import subprocess
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def _get_modifed_notebooks():
    """Returns a list of paths to modified noteooks."""
    git_diff = subprocess.run(
        ['git', 'diff', '--name-only', 'origin/main', '--', '*.ipynb'],
        capture_output=True,
        text=True,
        check=True
    )
    notebook_paths = git_diff.stdout.splitlines()
    return [Path(line.strip()) for line in notebook_paths if line.strip()]


def run_notebooks(notebook_paths):
    for notebook_path in notebook_paths:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(notebook, resources={'metadata': {'path': notebook_path.parent}})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--notebook-path', type=str, help='Path to the notebook to test.')
    args = parser.parse_args()
    if args.path is None:
        notebooks_to_test = _get_modifed_notebooks()
    else:
        notebooks_to_test = [args.notebook_path]

    run_notebooks(notebooks_to_test)
