# Contributing Guide

Thank you for your interest in contributing! This repository hosts tutorial and guide notebooks that are automatically published to our [FILL THIS IN LATER]. Please follow the steps below when adding a new cookbook.

---

## Adding a New Notebook

Each new notebook should be treated as its own contribution and added under the `tutorials/` directory.

### 1. Create a New Branch

Before making any changes, create a new branch with the following branch naming scheme:

```bash
git checkout -b new-cookbook-your-notebook-title
```

---

## Notebook Placement

Add your new `.ipynb` file inside the appropriate folder under:

```
tutorials/
```

If the tutorial belongs to an existing category, place it in that folder. If it introduces a new category, create a new folder with a clear name. For example, if you are adding a new notebook on CAG, you should put it in the `tutorials/CAG` folder.

---

## Update the Catalog

Every notebook must be registered so it appears on the site.

Edit the file:

```
catalog.yaml
```

Add a new entry with the following fields:

```yaml
- title: "Your Notebook Title"
  date: YYYY-MM-DD
  path: tutorials/<folder>/<your_notebook>.ipynb
  author: Great Writer
```

Ensure:

* The title matches the notebook's internal title.
* The date is today's date.
* The path is correct and relative to the repository root.

---

## Update the authors.yaml

If this notebook is written by a new author, update the [authors.yaml](https://github.com/datacebo/datacebo-cookbook/blob/main/authors.yaml) with their name, GitHub account and LinkedIn account (if applicable). The header for the entry should be in the format: `{first_name}{last_name}-{org}`.

---

## Update the requirements.txt

If any new requirements are needed for the notebook to run, add them to the [requirements.txt](https://github.com/datacebo/datacebo-cookbook/blob/main/requirements.txt).

---

## Commit and Push

```bash
git add .
git commit -m "Add new notebook: <your title>"
git push origin <your branch>
```

---

## Open a Pull Request

Open a PR using the following title format:

```
New Cookbook: <Your Notebook Title>
```

In the PR description, please include:

* A short summary of the notebook's purpose.
* Any new dependencies introduced.
* Any structural changes (e.g., new folder).

---

## Validate Your Notebook

When a PR is opened, a workflow will launch that will run your notebook end to end. If it fails, you must fix your notebook to ensure it passes.
