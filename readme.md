# ArcadIA Library

Library to add artificial intelligence and automated planning to small games.
To run, first you must install [pipenv](https://github.com/pypa/pipenv). Then, using the pipfile in the root folder, you must install the dependencies by running:

```
pipenv install -d
```

Then, you must be able to run python tests:

python -m pytest --cov  --cov-report=xml:coverage.xml --junitxml=junit.xml

(**NOT READY YET**)
To compile:

python setup.py build_ext --inplace