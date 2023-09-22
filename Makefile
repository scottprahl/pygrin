lint:
	-ruff check .
	-yamllint .github/workflows/*

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
	rm -rf docs/.ipynb_checkpoints
	rm -rf pygrin.egg-info
	rm -rf pygrin/__pycache__
	rm -rf tests/__pycache__

test:
	pytest --verbose tests/test_pygrin.py

testall:
	make clean
	make test
	pytest --verbose tests/test_all_notebooks.py
	rm -rf __pycache__

rcheck:
	make clean
	make testall
	make lint
	make pycheck
	make doccheck
	touch docs/*ipynb
	touch docs/*rst
	make html
	check-manifest
	pyroma -d .
