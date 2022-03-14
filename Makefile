SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build

pycheck:
	-pylint pygrin/pygrin.py
	-pylint pygrin/__init__.py

doccheck:
	-pydocstyle pygrin/pygrin.py
	-pydocstyle pygrin/__init__.py

html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	open docs/_build/index.html

clean:
	rm -rf dist
	rm -rf pygrin.egg-info
	rm -rf pygrin/__pycache__
	rm -rf docs/_build
	rm -rf docs/api
	rm -rf .tox
	rm -rf build
	rm -rf 

notecheck:
	make clean
	pytest --verbose test_all_notebooks.py
	rm -rf __pycache__

rcheck:
	make clean
	make pycheck
	make doccheck
	make notecheck
	touch docs/*ipynb
	touch docs/*rst
	make html
	check-manifest
	pyroma -d .
	tox

.PHONY: clean check rcheck html