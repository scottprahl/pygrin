pycheck:
	-pylint pygrin/pygrin.py
	-pylint pygrin/__init__.py

doccheck:
	-pydocstyle pygrin/pygrin.py
	-pydocstyle pygrin/__init__.py

html:
	cd docs && python -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build
	open docs/_build/index.html

clean:
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf build
	rm -rf dist
	rm -rf docs/_build
	rm -rf docs/api
	rm -rf docs/.ipynb-checkpoints
	rm -rf pygrin.egg-info
	rm -rf pygrin/__pycache__
	rm -rf tests/__pycache__

notecheck:
	make clean
	pytest --verbose tests/test_all_notebooks.py
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

.PHONY: clean check rcheck html