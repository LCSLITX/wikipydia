upload_pkg:
	python3 -m twine upload --repository testpypi dist/*

build:
	python3 -m build