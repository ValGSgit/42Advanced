# ex00 — Package management (conda / pip)

## The big idea
Python environments live in isolation: each env has its own interpreter and
packages. `conda` and `pip` are the two main tools to manage them.

| task                  | conda command                            | pip command              |
|-----------------------|------------------------------------------|--------------------------|
| list packages         | `conda list`                             | `pip list`               |
| show package info     | `conda search numpy --info`              | `pip show numpy`         |
| remove a package      | `conda remove numpy`                     | `pip uninstall numpy`    |
| install a package     | `conda install numpy`                    | `pip install numpy`      |
| freeze environment    | `conda env export > environment.yml`     | `pip freeze > req.txt`   |

## Things to understand before coding

1. **`environment.yml` vs `requirements.txt`.** conda exports to YAML and
   captures channels + conda deps; pip exports a flat list. For conda-managed
   envs, `environment.yml` is the right format.

2. **`--no-builds` flag.** `conda env export --no-builds` drops build-string
   suffixes so the file is portable across OS/CPU variants.

3. **Recreating from a file.**
   - conda: `conda create -n myenv --file requirements.txt`
   - pip:  `pip install -r requirements.txt`

4. **Why separate envs?** Different projects can need conflicting package
   versions. Environments keep them from stepping on each other.

## Self-check
Run `conda list | head` to confirm your active env has packages listed.
Run `pip show numpy` and spot the Version/Location fields.
