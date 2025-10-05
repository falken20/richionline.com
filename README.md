<div align="center">
<img src="./static/assets/logo_app.png" alt="drawing" width="400"/>
<a href="https://richionline-portfolio.nw.r.appspot.com"><img src="./static/assets/falken/falken_logo_ia_original.png" width=50 alt="Personal Portfolio web"></a>

![Version](https://img.shields.io/badge/version-1.0.1-blue) ![GitHub language count](https://img.shields.io/github/languages/count/falken20/richionline.com) ![GitHub Top languaje](https://img.shields.io/github/languages/top/falken20/richionline.com) ![Test coverage](https://img.shields.io/badge/test%20coverage-100%25-brightgreen) ![GitHub License](https://img.shields.io/github/license/falken20/richionline.com)


[![Richi web](https://img.shields.io/badge/web-richionline-blue)](https://richionline-portfolio.nw.r.appspot.com) [![Twitter](https://img.shields.io/twitter/follow/richionline?style=social)](https://twitter.com/richionline)

</div>



Flask web for personal portfolio

---

##### Endpoint
https://richionline-portfolio.nw.r.appspot.com

##### Deploy in Google Cloud Platform

```bash
gcloud app deploy
```

##### Setup

```bash
pip install -r requirements.txt
```

##### Running the app

```bash
flask run (with .flaskenv)
```
or
```
flask run -app PATH_APP
```

##### Setup tests

```bash
pip install -r requirements-tests.txt
```

##### Running the tests

Run all tests with pytest:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run tests with coverage report:
```bash
pytest --cov=. --cov-report=html --cov-report=term-missing
```

Run specific test file:
```bash
pytest tests/test_main.py
```

Run specific test class or function:
```bash
pytest tests/test_main.py::TestHomeRoute::test_home_status_code
```

##### Running the tests with pytest and coverage

```bash
./scripts/check_project.sh
```
or
```bash
coverage run -m pytest -v && coverage html --omit=*/venv/*,*/tests/*
```

##### Test Coverage

The test suite includes:
- **Route Tests**: Tests for all Flask routes (home, contact, portfolio)
- **Configuration Tests**: Tests for config.py constants and SETUP_DATA
- **Template Tests**: Verification that correct templates are rendered
- **Error Handling Tests**: Tests for 404 and invalid HTTP methods
- **Static Files Tests**: Basic tests for static file serving

View the detailed coverage report by opening `htmlcov/index.html` after running tests with coverage.
---

##### Versions

1.0.1 Some new styles and config
1.0.0 First version
