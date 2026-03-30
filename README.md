# Flask TODO App - Capstone Testing Project

## Project Overview
This repository contains the capstone testing project for **CMP1979 Modern Software Development**. 
The group has completed a focused black-box and white-box testing engagement on the **Flask TODO App**, 
a simple task management web application.

---

## Group Members
- **Melonie Matho Mboh** (A00314636) – Quality Analysis & Tracking Lead
- **Aaron Abeiku Ackon** (A00310246) – Automation & Repository Lead
- **Charles Nnebedum** (A00331872) – Test Design & Documentation Lead

---

## Application Under Test
**Flask TODO App** – A lightweight, full-stack task management web application built with Flask and SQLite.

### Key Features
- User registration and authentication (login/logout)
- Task creation and deletion with confirmation
- Task lifecycle management (status cycling: Pending → Working → Done)
- Bulk task deletion via "Clear All Tasks" button
- User profile display

### Repository
**Original Project:** https://github.com/Swappy514/Flask-TODO-APP

---

## Project Summary
This testing project focuses on three core workflows:
1. **User Authentication** – Registration, login, logout
2. **Task Management** – Creating and deleting tasks
3. **Task Lifecycle Management** – Status transitions and bulk deletion

### Key Testing Activities
- **Black-Box Testing:** Equivalence partitioning and boundary value analysis on forms
- **White-Box Testing:** Code-level analysis of authentication and task logic
- **Exploratory Testing:** Two time-boxed sessions on edge cases and defect discovery
- **Static Analysis:** PEP 8 and code quality checks using flake8 and pylint
- **Automated Testing:** UI-level and unit-level tests using Playwright and pytest
- **Non-Functional Testing:** Accessibility compliance (WCAG 2.1)

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Flask-TODO-APP-Testing.git
cd Flask-TODO-APP-Testing
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
```bash
# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Run the app
flask run
```
The application will be available at `http://localhost:5000`

### 4. Run the Automated Tests
```bash
# Run all tests
pytest

# Run only unit tests
pytest tests/unit/

# Run only UI tests
pytest tests/ui/

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/unit/test_task_lifecycle.py
```

### 5. Run Static Analysis
```bash
# Run flake8
flake8 app/

# Run pylint
pylint app/auth.py app/tasks.py
```

---

## Repository Structure
Flask-TODO-APP/
│
├── app/                          # Application source code (original Flask app)
│   ├── __init__.py               # App factory and Flask configuration
│   ├── models.py                 # SQLAlchemy models (User, Task)
│   ├── auth/                     # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── routes.py             # Register, login, logout routes
│   │   └── forms.py              # WTForms for login and registration
│   ├── tasks/                    # Task management blueprint
│   │   ├── __init__.py
│   │   ├── routes.py             # Task creation, deletion, status cycling
│   │   └── forms.py              # Task input form
│   ├── profile/                  # User profile blueprint
│   │   ├── __init__.py
│   │   └── routes.py             # Profile display route
│   ├── static/                   # CSS and static assets
│   └── templates/                # Jinja2 HTML templates
│       ├── base.html
│       ├── auth/
│       ├── tasks/
│       └── profile/
│
├── instance/                     # SQLite database (auto-generated, gitignored)
│   └── todo.db
│
├── tests/                        # All testing artifacts (added by our group)
│   ├── ui/                       # Playwright end-to-end UI tests
│   │   ├── test_login_logout.py  # TC-AUTH-01: Valid login and logout flow
│   │   └── test_task_crud.py     # TC-TASK-01: Task creation and deletion
│   ├── unit/                     # pytest unit tests
│   │   └── test_task_status.py   # TC-LIFE-01: Status cycling logic (Pending→Working→Done)
│   └── conftest.py               # Shared fixtures and test configuration
│
├── evidence/                     # Testing evidence and artifacts
│   ├── screenshots/              # Screenshots from exploratory and UI testing
│   ├── static-analysis/          # flake8 and pylint output logs
│   ├── accessibility/            # axe DevTools accessibility scan results
│   └── models/                   # State transition diagram image
│
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions: automated test and lint pipeline
│
├── .gitignore
├── LICENSE
├── README.md                     # This file
├── requirements.txt              # Python dependencies (Flask, Playwright, pytest, flake8, pylint)
└── run.py                        # Application entry point

   ── tests.yml # GitHub Actions CI/CD
 ── app/ # Original application code
├── auth.py # Authentication logic
 ── tasks.py # Task management logic
└── ...
