# Contributing to {{ cookiecutter.package_distribution_name }}

## Set up for development

Activate a Python 3.11 or newer virtual environment and run:

```sh
python -m pip install -e .
```

## Run the tests

Run the following command and expect `Hello, Hee!`:

```sh
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```

## Send a change

1. Start from `main`, create a branch, and commit your change.
2. Push your branch to GitHub.
3. Open a pull request from your branch into `main`.
