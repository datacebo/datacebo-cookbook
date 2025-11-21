import argparse
import os

import nbformat
from nbconvert.exporters import HTMLExporter

from scripts.utils import _get_modifed_notebooks


def convert_notebooks_to_html(notebook_paths):
    for notebook_path in notebook_paths:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        filename = os.path.basename(notebook_path)
        html_exporter = HTMLExporter()
        html_exporter.exclude_input = False  # keep code cells; set True to hide them
        body, _ = html_exporter.from_notebook_node(notebook)
        with open(f'{filename}.html', 'w', encoding='utf-8') as f:
            f.write(body)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--notebook-path', type=str, help='Path to the notebook to test.')
    args = parser.parse_args()
    if args.notebook_path is None:
        notebooks_to_test = _get_modifed_notebooks(mode='commit')
    else:
        notebooks_to_test = [args.notebook_path]

    convert_notebooks_to_html(notebooks_to_test)
