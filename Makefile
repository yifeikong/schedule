build:
	python setup.py sdist bdist_wheel --universal

pypi:
	twine upload dist/*

clean:
	rm -rf build/ dist/ sche.egg-info/

init:
	( \
		pip install -r requirementes-dev.txt \
		pip install -U twine wheel \
	)
