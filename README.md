## JS Unit Testing Task (Python Version)

This project is a Python implementation of a JavaScript unit testing assignment provided by a recruiter. The original task involved writing and executing unit tests for utility functions typically used in web applications. Since I currently work with Python and have limited exposure to JavaScript, I've completed the task using Python and pytest.

## Project Structure

js-task-python-version/
│
├── src/
│ └── utils.py # Core utility functions
│
├── tests/
│ └── test_utils.py # Unit tests using pytest
│
├── htmlcov/ # HTML test coverage report (generated)
├── README.md # Project overview and instructions
└── requirements.txt # Python dependencies

## Functions Tested

1. calculate_discount(price, discount)
2. filter_products(products, query)
3. sort_products(products, key)
4. validate_email(email)

Each function is tested for:
- Valid and invalid inputs
- Edge cases
- Error handling

## Tools & Frameworks Used

- Python 3.10
- [pytest](https://docs.pytest.org/)
- [coverage.py](https://coverage.readthedocs.io/)

## How to Run the Tests

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run tests with coverage
coverage run -m pytest

# Generate HTML coverage report
coverage html

# View the report
start htmlcov/index.html  # On Windows

## Assumptions

- This project replicates the JavaScript task as closely as possible in Python.
- I’ve prioritized accuracy, readability, and modular design.
- No asynchronous or external dependencies were required for these specific functions.

## Why Python?
- While the task originally asked for JavaScript, I opted to implement this in Python as I’m currently working on test automation using Python-based tools like Selenium and Playwright.
- I’m open to learning JavaScript-based automation as my next step and welcome guidance or upskilling opportunities.

## Test Coverage
A full test coverage report is available inside the htmlcov/ directory.

You can open it by running:
start htmlcov/index.html

## Author
Satya Venkata Gangadhar Samanthula
QA Engineer
ssvgangadhar@gmail.com


