# ex04 — MiniPack (build a pip-installable package)

## The big idea
Turn your code into a real installable package `my_minipack` with two modules:
- `my_minipack.progress`  -> your progress bar (MOD0 ex10, `ft_progress`)
- `my_minipack.logger`    -> your logger (MOD2 ex02, the `log` decorator)

Then build distribution files so it installs with:
```
pip install ./dist/my_minipack-1.0.0.tar.gz
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
```

## Folder layout (already scaffolded for you)
```
ex04/
├── build.sh
├── setup.cfg          <- all the metadata (name, author, classifiers...)
├── setup.py           <- tiny shim that calls setup()
├── pyproject.toml     <- declares the build system
├── LICENSE.md
├── README.md
└── my_minipack/
    ├── __init__.py
    ├── progress.py    <- paste your ft_progress here
    └── logger.py      <- paste your log decorator here
```

## What you need to do

1. **Fill the two modules.** Copy your own `ft_progress` into `progress.py` and
   your `log` decorator into `logger.py`. (Keep them as plain functions; drop the
   `if __name__ == "__main__"` demo blocks or guard them.)

2. **Edit the metadata** in `setup.cfg`: change author / email / summary /
   classifiers to your own. The subject explicitly says don't copy theirs.

3. **Understand build.sh.** It (a) upgrades pip, (b) makes sure `build`/`wheel`
   are available, (c) runs the build to produce `dist/*.tar.gz` and
   `dist/*.whl`. Read each line so you can explain it.

4. **Test in a clean venv** (this is the conclusion the subject wants you to draw
   — a fresh env starts with almost nothing, and installing your package adds it
   plus its build deps):
   ```
   python -m venv tmp_env && source tmp_env/bin/activate
   pip list                       # tiny: pip, setuptools
   bash build.sh
   ls dist                        # the .whl and .tar.gz
   pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
   pip list                       # now shows my-minipack 1.0.0
   pip show -v my_minipack        # your metadata
   python -c "import my_minipack.logger; import my_minipack.progress; print('ok')"
   deactivate
   ```

## Key concepts
- **sdist vs wheel.** `.tar.gz` (sdist) is the source; `.whl` (wheel) is the
  pre-built, faster-to-install form. You want both.
- **setup.cfg vs setup.py.** Modern packaging keeps metadata declaratively in
  `setup.cfg`; `setup.py` can shrink to a one-liner. `pyproject.toml` tells pip
  which build backend (setuptools) to use.
- **`packages = find:`** auto-discovers the `my_minipack` folder (it's a package
  because it has `__init__.py`).
