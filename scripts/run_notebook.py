import argparse
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

from scripts.utils import _get_modifed_notebooks


def run_notebooks(notebook_paths):
    for notebook_path in notebook_paths:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=3600, kernel_name='python3')

        ep.preprocess(notebook, resources={'metadata': {'path': Path(notebook_path).parent}})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--notebook-path', type=str, help='Path to the notebook to test.')
    args = parser.parse_args()
    if args.notebook_path is None:
        notebooks_to_test = _get_modifed_notebooks()
    else:
        notebooks_to_test = [args.notebook_path]

    run_notebooks(notebooks_to_test)
