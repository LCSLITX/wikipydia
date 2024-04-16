upload_pkg:
	python3 -m twine upload --repository testpypi dist/*

build:
	python3 -m build

lint:
	pylint src

unit-tests:
	python3 -m pytest --verbose

freeze:
	pip freeze > requirements.txt