SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build

check:
	-pylint pygrin/pygrin.py
	-pep257 --ignore D401 pygrin/pygrin.py
	-pylint pygrin/__init__.py
	-pep257 pygrin/__init__.py

html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean:
	rm -rf dist
	rm -rf pygrin.egg-info
	rm -rf pygrin/__pycache__
	rm -rf docs/_build/*
	rm -rf docs/_build/.buildinfo
	rm -rf docs/_build/.doctrees
	rm -rf docs/api/*
	rm -rf .tox
	rm -rf 

rcheck:
	make clean
	touch docs/*ipynb
	touch docs/*rst
	make html
	check-manifest
	pyroma -d .
	tox

.PHONY: clean check rcheck html