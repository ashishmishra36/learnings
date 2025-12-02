# E-Commerce Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-7.x-green.svg)](https://pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-brightgreen.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A robust, scalable test automation framework for E-Commerce applications using Page Object Model (POM), PyTest, and Selenium WebDriver.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Test Execution](#-test-execution)
- [Reporting](#-reporting)
- [CI/CD Integration](#-cicd-integration)
- [Architecture](#-architecture)
- [Best Practices](#-best-practices)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

This test automation framework is designed to test E-Commerce web applications with a focus on maintainability, scalability, and reusability. Built using the Page Object Model design pattern, it provides a clean separation between test code and page-specific code, making tests easier to maintain and extend.

### What This Framework Does

- ✅ Automates functional testing of E-Commerce applications
- ✅ Supports multiple browsers (Chrome, Firefox, Edge, Safari)
- ✅ Provides detailed HTML and Allure test reports
- ✅ Enables parallel test execution for faster feedback
- ✅ Integrates seamlessly with CI/CD pipelines
- ✅ Manages test data externally (Excel, JSON, CSV)

---

## ✨ Features

### Core Capabilities

- 🏗️ **Page Object Model (POM)**: Industry-standard design pattern for maintainable test code
- 🧪 **PyTest Framework**: Powerful testing framework with fixtures, parametrization, and plugins
- 🌐 **Cross-Browser Testing**: Support for Chrome, Firefox, Edge, and Safari
- 👻 **Headless Mode**: Execute tests without GUI for CI/CD environments
- ⚡ **Parallel Execution**: Run tests in parallel using pytest-xdist
- 📊 **Rich Reporting**: HTML and Allure reports with screenshots on failure
- 📝 **Comprehensive Logging**: Detailed logs for debugging and analysis
- 💾 **Data-Driven Testing**: External test data management (Excel, JSON, CSV)
- 🔧 **Configurable**: Centralized configuration management
- 🐳 **Docker Support**: Containerized test execution

### Test Coverage

- User Registration & Account Creation
- User Login & Authentication
- Product Search & Filtering
- Shopping Cart Operations
- Checkout Process
- Account Management
- Order History
- And more... (see `testcase.md`)

---

## 📦 Prerequisites

### Required Software

| Software | Version | Purpose |
|----------|---------|---------|
| Python | 3.13+ | Programming language |
| pip | Latest | Package manager |
| virtualenv | Latest | Virtual environment |
| Git | Latest | Version control |

### Optional Tools

| Tool | Purpose |
|------|---------|
| Allure CLI | Generate Allure reports |
| Docker | Containerized execution |
| Jenkins | CI/CD automation |

### Browser Drivers

Ensure you have the appropriate WebDriver for your browser:

- **ChromeDriver** for Google Chrome
- **GeckoDriver** for Mozilla Firefox
- **EdgeDriver** for Microsoft Edge

> **Note**: WebDriver Manager can auto-download drivers (included in dependencies)

---

## 🚀 Quick Start

Get up and running in 5 minutes:
1. Clone the repository
git clone https://github.com/ashishmishra36/learnings.git cd learnings/ecommerce
2. Create and activate virtual environment
python -m venv .venv source .venv/bin/activate # On Windows: .venv\Scripts\activate
3. Install dependencies
pip install -r ../requirements.txt
4. Run tests
cd tests pytest -v --browser chrome

## Project Structure

    ecommerce/
    │
    ├── pages/                          # Page Object Model classes
    │   ├── __init__.py
    │   ├── base_page.py               # Base page with reusable methods
    │   ├── home_page.py               # Home page objects
    │   ├── login_page.py              # Login page objects
    │   ├── register_page.py           # Registration page objects
    │   ├── account_page.py            # Account page objects
    │   └── success_registration.py    # Success page objects
    │
    ├── tests/                          # Test suites
    │   ├── __init__.py
    │   ├── conftest.py                # PyTest fixtures & configuration
    │   ├── base_test.py               # Base test class
    │   ├── test_home_page.py          # Home page tests
    │   ├── test_login.py              # Login tests
    │   ├── test_register.py           # Registration tests
    │   ├── test_account.py            # Account management tests
    │   ├── test_success_registeration.py
    │   └── reports/                   # Test reports directory
    │       ├── report.html            # HTML report
    │       └── allure_results/        # Allure results
    │
    ├── configs/                        # Configuration files
    │   ├── __init__.py
    │   ├── config.py                  # Application configuration
    │   └── data.xlsx                  # Test data (Excel)
    │
    ├── utils/                          # Utility modules
    │   ├── __init__.py
    │   ├── logger.py                  # Logging configuration
    │   ├── util_excel.py              # Excel utilities
    │   └── util_pages.py              # Page utilities
    │
    ├── reports/                        # Generated reports
    │   ├── report.html                # HTML test report
    │   └── allure_results/            # Allure results
    │
    ├── screenshots/                    # Failure screenshots
    │
    ├── pytest.ini                     # PyTest configuration
    ├── jenkinsfile                    # Jenkins pipeline
    ├── jenkinsfile_V0                 # Jenkins pipeline (v0)
    ├── DOCKER.md                      # Docker instructions
    ├── testcase.md                    # Test case documentation
    ├── project.puml                   # UML diagrams
    └── README.md                      # This file



## 📊 Reporting
    HTML Reports (pytest-html)
    Location: tests/reports/report.html
    Features:
    ✅ Test execution summary
    ✅ Pass/Fail/Skip counts
    ✅ Execution time per test
    ✅ Error messages & stack traces
    ✅ Environment information
    ✅ Self-contained (portable)
    Screenshot:
    ┌─────────────────────────────────────┐
    │  Test Report Summary                │
    ├─────────────────────────────────────┤
    │  Total: 25  Passed: 23  Failed: 2   │
    │  Duration: 2m 34s                   │
    └─────────────────────────────────────┘


Allure Reports
    Location: tests/reports/allure_results/
    Features:
    📊 Interactive dashboard
    📈 Trend analysis
    🔍 Detailed test steps
    📸 Screenshots on failure
    🏷️ Categorization
    ⏱️ Performance metrics
    🎯 Flaky test detection
    📅 Historical data


### Screenshots on Failure
    Failed tests automatically capture screenshots:
    **Location**: `screenshots/{test_name}_{timestamp}.png`
    **Configuration** (in `conftest.py`):


### Logging
    **Log Levels**: DEBUG | INFO | WARNING | ERROR | CRITICAL
    **Configuration** (in `utils/logger.py`):



## 🔄 CI/CD Integration
    Jenkins Pipeline
    Pipeline File: jenkinsfile
    Pipeline Stages:
    ┌──────────────┐
    │   Checkout   │  Clone repository
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │    Setup     │  Create venv, install deps
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │  Run Tests   │  Execute test suite
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │   Reports    │  Generate HTML/Allure reports
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │   Archive    │  Save artifacts
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │   Publish    │  Upload to S3
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │   Notify     │  Send email
    └──────────────┘



### Docker Support
    See `DOCKER.md` for Docker setup instructions.
    **Quick Docker Run**:
    
    # Build image
    docker build -t ecommerce-tests .
    
    # Run tests
    docker run --rm ecommerce-tests
    
    # Run with custom browser
    docker run --rm -e BROWSER=firefox ecommerce-tests


### 🏗️ Architecture
        Framework Architecture
        ┌─────────────────────────────────────────────────────────┐
        │                   Test Layer                             │
        │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
        │  │  Login   │  │ Register │  │   Home   │              │
        │  │  Tests   │  │  Tests   │  │  Tests   │   ...        │
        │  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
        └───────┼─────────────┼─────────────┼────────────────────┘
                │             │             │
                └─────────────┼─────────────┘
                              │ inherits from
                ┌─────────────▼─────────────┐
                │      BaseTest Class        │
                │  - setup/teardown          │
                │  - common utilities        │
                └─────────────┬───────────────┘
                              │ uses
                ┌─────────────▼─────────────┐
                │   PyTest Fixtures          │
                │  (conftest.py)             │
                │  - init_driver             │
                │  - screenshot_on_failure   │
                └─────────────┬───────────────┘
                              │ creates
                ┌─────────────▼─────────────┐
                │      WebDriver             │
                │  (Chrome/Firefox/Edge)     │
                └─────────────┬───────────────┘
                              │ controls
        ┌─────────────────────▼─────────────────────────────────┐
        │              Page Object Model Layer                   │
        │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
        │  │ BasePage │◄─┤LoginPage │◄─┤HomePage  │            │
        │  │          │  │          │  │          │            │
        │  │ Common   │  │ Locators │  │ Locators │            │
        │  │ Methods  │  │ Actions  │  │ Actions  │   ...      │
        │  └──────────┘  └──────────┘  └──────────┘            │
        └───────────────────┬───────────────────────────────────┘
                            │ uses
        ┌───────────────────▼───────────────────────────────────┐
        │              Utilities & Config Layer                  │
        │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
        │  │  Logger  │  │  Config  │  │  Excel   │            │
        │  │          │  │          │  │  Utils   │            │
        │  └──────────┘  └──────────┘  └──────────┘            │
        └───────────────────────────────────────────────────────┘

### Test Execution Flow
    1. Test Discovery
       └── PyTest discovers test_*.py files
       
       2. Fixture Setup (conftest.py)
          └── init_driver fixture
              ├── Read browser config
              ├── Initialize WebDriver
              ├── Set timeouts
              └── Inject driver into test class
       
       3. Test Class Setup (BaseTest)
          └── setUp method
              ├── Maximize window
              ├── Navigate to base URL
              └── Initialize page objects
       
       4. Test Execution
          └── Test method runs
              ├── Page objects perform actions
              ├── Assertions verify results
              └── Log test steps
       
       5. Test Teardown
          └── tearDown method
              ├── Capture screenshot (if failed)
              ├── Clear cookies
              └── Close browser
       
       6. Report Generation
          └── Generate HTML/Allure reports

🔧 Troubleshooting



## Code Style

   1. Follow PEP 8 style guide
   2. Use meaningful variable/function names
   3. Add docstrings to classes and methods
   4. Keep methods focused and short
   5. Write self-documenting code

## Pull Request Checklist

   1. Code follows project style guidelines
   2. Tests pass locally
   3. New tests added for new features
   4. Documentation updated
   5. Commit messages are meaningful
   6. o merge conflicts