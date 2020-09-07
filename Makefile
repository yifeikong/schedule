build:
	python setup.py sdist bdist_wheel --universal

pypi:
	twine upload dist/*

clean:
	rm -rf build/ dist/ sche.egg-info/
