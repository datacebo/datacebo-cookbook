import argparse
import os
import logging
from pathlib import Path

import nbformat
from traitlets.config import Config
from nbconvert.exporters import HTMLExporter

os.environ['SDMETRICS_PLOTLY_RENDERER'] = 'png'

logger = logging.getLogger(__name__)

def get_all_notebook_paths():
    notebook_paths = list(Path(os.getcwd()).rglob("*.ipynb"))
    return notebook_paths

def convert_notebooks_to_html(notebook_paths, only_new=True):
    c = Config()
    c.CSSHTMLHeaderPreprocessor.style = 'material'
    c.TemplateExporter.exclude_input_prompt = True
    c.TemplateExporter.exclude_output_prompt = True
    c.ExecutePreprocessor.enabled = True
    c.ExecutePreprocessor.timeout = 3600

    docs_dir = Path(os.getcwd()) / 'docs'
    for notebook_path in notebook_paths:
        parent_folder = notebook_path.parent
        filename = os.path.splitext(os.path.basename(notebook_path))[0]
        html_docs_path = docs_dir / f'{parent_folder.name}/{filename}.html'
        html_file_path = parent_folder /f'{filename}.html'
        if only_new and html_docs_path.exists():
            logger.info(f'Skipping {filename} because {html_docs_path} already exists.')
            continue

        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        os.chdir(parent_folder)
        html_exporter = HTMLExporter(config=c)
        html_exporter.exclude_input = False
        body, _ = html_exporter.from_notebook_node(notebook)
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(body)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--all',
        action='store_true',
        default=False,
        help='Whether to run all notebooks or only the ones that do not already have an HTML file.'
    )
    args = parser.parse_args()
    only_new = not(args.all)

    notebook_paths = get_all_notebook_paths()
    convert_notebooks_to_html(notebook_paths, only_new=only_new)
