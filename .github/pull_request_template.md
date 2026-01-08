## For new cookbooks

If you are adding a new cookbook, make sure the following requirements are met:

- [ ] A new notebook was added in an appropriate directory.
- [ ] An entry was made in the [catalog.yaml](https://github.com/datacebo/datacebo-cookbook/blob/main/registry.yaml) for this notebook. Make sure the following conditions are met:
  - [ ] A title was added for the notebook
  - [ ] A file path was added for the notebook. This should be relative to the `datacebo-cookbook` directory (eg. tutorials/synthesizing/SDV_Synthesize_a_table_Gaussian_Copula.ipynb)
  - [ ] A date for the addition of the notebook. Should be the date corresponding to when you open the PR.
  - [ ] An author was added for the notebook.
  - [ ] An appropriate tag from TAG.md was added to describe the notebook. 
- [ ] If any new dependencies are required for the notebook to run successfully, they should be added to the [requirements.txt](https://github.com/datacebo/datacebo-cookbook/blob/main/requirements.txt).
- [ ] The `Run Modified Notebooks` workflow should pass.
