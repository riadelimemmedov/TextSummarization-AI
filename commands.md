# All commands using project

Project requirements

- Create virtual environment for python 3.12:
  - `python3.12 -m venv env`
- Activate virtual environment:
  - `source env/bin/activate`
- Write all environment packages to requirements file:
  - `pip freeze > requirements.txt`
- Install all dependencies from requirements file:
  - `pip install -r requirements.txt`

Backend

- Run tests with code coverage:
  - `poetry run coverage run -m pytest`
- Run tests:
  - `poetry run pytest`
- Run tests with coverage:
  - `poetry run pytest --cov`
- Run tests with output capturing disabled:
  - `poetry run pytest -s`
- Run specific file:
  - `poetry run pytest -k`
- Run tests until failure:
  - `poetry run pytest -x`
- Run tests paralel:
  - `poetry run pytest -n auto`
- Format code using Black:
  - `poetry run black .`
- Generate html for covering tests:
  - `poetry run pytest --cov=./ --cov-report=html`
- Check code formatting is needed or not:
  - `poetry run black . --check`
- Sor t imports using isort with Black profile:
  - `poetry run isort . --profile black`
- Check code style with Flake8:
  - `poetry run flake8 .`
- Check code bug:
  - `poetry run bandit .`
- Run pre commit hooks
- `poetry run pre-commit run --all-files`
- Stress test using Apache Benchmark
- `ab -n 400 -c 10 http://127.0.0.1:8000/ping/`
