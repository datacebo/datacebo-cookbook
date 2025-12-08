import os
from pathlib import Path

import nbformat
from traitlets.config import Config
from nbconvert.exporters import HTMLExporter


def get_all_notebook_paths():
    notebook_paths = list(Path(os.getcwd()).rglob("*.ipynb"))
    return notebook_paths

def convert_notebooks_to_html(notebook_paths):
    c = Config()
    c.CSSHTMLHeaderPreprocessor.style = 'material'
    for notebook_path in notebook_paths:
        parent_folder = notebook_path.parent
        filename = os.path.splitext(os.path.basename(notebook_path))[0]
        html_file_path = parent_folder / f'{filename}.html'
        # if html_file_path.exists():
        #     continue

        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        html_exporter = HTMLExporter(config=c)
        html_exporter.exclude_input = False
        body, _ = html_exporter.from_notebook_node(notebook)
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(body)


if __name__ == '__main__':
    notebook_paths = get_all_notebook_paths()
    convert_notebooks_to_html(notebook_paths)
