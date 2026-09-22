# SauceDemo Automation Suite

A production-ready Selenium UI test automation framework for [Sauce Demo](https://www.saucedemo.com/), built with **Python** and **pytest** following the **Page Object Model** design pattern.

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Language |
| Selenium 4 | Browser automation |
| pytest | Test runner |
| pytest-html | HTML test reports |
| ChromeDriver | Auto-managed via Selenium Manager |

## Project Structure

```
SauceDemo-Automation-Suite/
├── src/
│   ├── main/
│   │   └── python/
│   │       └── org/example/
│   │           └── main.py            # Standalone script entry point
│   └── test/
│       └── python/
│           ├── conftest.py            # Path configuration for pytest
│           ├── first_test.py          # Smoke test script
│           ├── base/
│           │   └── base_test.py       # Driver setup / teardown
│           ├── pages/
│           │   ├── login_page.py
│           │   ├── product_page.py
│           │   ├── cart_page.py
│           │   └── checkout_page.py
│           └── tests/
│               ├── test_login.py
│               ├── test_product.py
│               ├── test_cart.py
│               └── test_checkout.py
├── reports/                           # Auto-generated HTML reports
├── requirements.txt
├── pytest.ini
└── README.md
```

## Prerequisites

- Python 3.10+
- Google Chrome installed
- Selenium Manager (included in Selenium 4.6+) handles ChromeDriver automatically — no manual setup required

## Setup

```bash

# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests (generates HTML report in reports/)
pytest

# Run a specific test file
pytest src/test/python/tests/test_login.py

# Run a specific test method
pytest src/test/python/tests/test_login.py::TestLogin::test_valid_login

# Run without HTML report
pytest -v --no-header --override-ini="addopts="
```

## Test Cases

| Test Class | Test Method | Description |
|---|---|---|
| `TestLogin` | `test_valid_login` | Successful login redirects to inventory page |
| `TestProduct` | `test_add_product_to_cart` | Product page loads and cart badge updates to 1 |
| `TestCart` | `test_remove_product_from_cart` | Item added then removed from cart |
| `TestCheckout` | `test_complete_checkout` | End-to-end checkout flow completes successfully |

## Design Pattern

**Page Object Model (POM)** — locators and interactions are encapsulated in dedicated page classes. Tests remain clean and readable, with zero locator logic leaking into test files.

## Reports

After a test run, open the auto-generated HTML report:

```
reports/report.html
```

## License

[MIT](LICENSE)
