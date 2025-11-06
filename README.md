# Stores REST API (Flask)

![Build Status](https://github.com/rylub/stores-rest-api-test/actions/workflows/tests.yml/badge.svg)

A RESTful API built with Flask and Flask-RESTful to manage stores and items. This project includes authentication, database persistence, and automated testing through GitHub Actions. It follows a clean, modular structure and demonstrates industry-standard practices for API design and quality assurance.

---

## Overview

This project implements a fully functional REST API for managing stores and their items. It provides endpoints for creating, reading, updating, and deleting stores, as well as managing items associated with each store. The API is secured with JWT-based authentication and backed by a relational database using SQLAlchemy ORM.

All tests are executed automatically on every push through GitHub Actions to ensure reliability and maintain code quality.

---

## Features

- Flask RESTful API design
- JWT-based authentication
- SQLAlchemy ORM for database persistence
- Integration and unit tests using pytest
- Continuous Integration via GitHub Actions
- Clean modular architecture for scalability

---

## Project Structure

```
starter_code/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .venv/
│
├── instance/
│   └── data.db
│
├── starter_code/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   ├── run.py
│   ├── security.py
│   ├── readme.md
│   ├── requirements.txt
│   │
│   ├── models/
│   │   ├── item.py
│   │   ├── store.py
│   │   └── user.py
│   │
│   ├── resources/
│   │   ├── auth.py
│   │   ├── item.py
│   │   ├── store.py
│   │   └── user.py
│   │
│   └── tests/
│       ├── base_test.py
│       ├── integration/
│       ├── system/
│       └── unit/
│
├── .flaskenv
├── .gitignore
├── Export.postman_collection.json
└── export.postman_environment.json
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rylub/stores-rest-api-test.git
   cd stores-rest-api-test/starter_code
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate   # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   flask run
   ```

The API will be available at `http://127.0.0.1:5000/`.

---

## Running Tests

All tests are written using `pytest`.

To run tests locally:
```bash
pytest
```

Tests include:
- Unit tests for models
- Integration tests for API resources
- System tests for full request flows

GitHub Actions runs these tests automatically on every push to ensure consistency.

---

## Continuous Integration

This project uses GitHub Actions for automated testing.  
The workflow file is located in `.github/workflows/tests.yml`.

Every push triggers:
1. Python environment setup
2. Dependency installation
3. Test execution with pytest
4. Status reporting on the repository

---

## Caching Dependencies in CI

To speed up builds in GitHub Actions, you can cache pip dependencies. Add the following step before installing dependencies in `.github/workflows/tests.yml`:

```yaml
      - name: Cache pip dependencies
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
```

This ensures dependencies are reused across builds unless `requirements.txt` changes.

---

## Dependencies

Key packages used in this project:
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-SQLAlchemy
- psycopg2
- pytest

---

## Future Improvements

- Add Swagger/OpenAPI documentation
- Implement role-based authorization
- Add logging and error tracking
- Expand test coverage for edge cases
- Dockerize the application for easier deployment

---

## License

This project is for educational and demonstration purposes.  
You are free to use or modify it as a learning resource.