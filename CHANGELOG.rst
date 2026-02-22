Changelog
=========

Unreleased ()
-------------
* migrate Makefile from venv bootstrap prerequisites to uv
* add shared Makefile target lists for pylint, yaml, rst, and test target definitions
* raise supported Python range to 3.10-3.14 and align CI/runtime defaults to 3.14 where non-matrix
* update docs and JupyterLite extras to current compatible range-based dependency specs

0.6.1 (2026-01-05)
------------------
* remove requirements*.txt, all deps in pyproject.toml
* version info only in __init__.py
* update readthedocs configuration
* update github action to publish to pypi
* fix pylint warnings in update_citation.py
* update zenodo url

0.6.0 (2025-11-17)
------------------
* support jupyterlite
* eliminate setup.cfg and setup.py
* use black for formatting
* update README

0.5.1 (2023-09-22)
------------------
* fix inconsistent python requires

0.5.0 (2023-09-22)
------------------
* no new features, just updating packaging
* add conda-forge support
* add zenodo DOI citation support
* add github action workflows
* add trivial test file

v0.4.4 (2021-08-06)
-------------------
* create pure python packages
* include .whl file
* package as python3 only

v0.4.3 (2021-01-12)
-------------------
* improve help(pygrin)
* improve html at https://pygrin.readthedocs.io
* use google docstrings again

v0.4.1 (2020-05-19)
-------------------
* update function parameters for sphinx automodapi

v0.4.0 (2020-05-19)
-------------------
* sphinx documentation
* `plot_principal_plt` -> `plot_principal_planes`

v0.3.0 (2020-01-22)
-------------------
* renamed `pitch()` to `period()` to avoid stepping on the name.
* improve readme
* fix `pylint` warnings
* fix `pep257` warnings
* fix `pyroma` warnings

v0.2.0 (2018-03-04)
-------------------
* improve description
* add `hyperbolic_secant_profile_index`
* fix importing, update for new names

v0.1.0 (2018-01-16)
-------------------
* fix typos
* change status to alpha
