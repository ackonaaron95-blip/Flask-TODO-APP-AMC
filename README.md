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
├── app/                              # Main Flask application package
│   ├── __init__.py                   # App factory and application setup
│   ├── models.py                     # Database models for users and tasks
│   ├── static/                       # Static assets such as CSS, JS, and images
│   ├── templates/                    # HTML templates rendered by Flask
│   ├── auth/                         # Authentication module / blueprint
│   │   ├── __init__.py
│   │   ├── forms.py                  # Login and registration forms
│   │   └── routes.py                 # Login, logout, and registration routes
│   ├── tasks/                        # Task management module / blueprint
│   │   ├── __init__.py
│   │   ├── forms.py                  # Task creation or update forms
│   │   └── routes.py                 # Create, view, update, and delete task routes
│   └── profile/                      # User profile module / blueprint
│       ├── __init__.py
│       └── routes.py                 # Profile-related routes
│
├── instance/                         # Instance-specific files such as local SQLite DB
│   └── todo.db                       # Local database file (may be generated at runtime)
│
├── tests/                            # Automated test files added for the capstone
│   ├── unit/                         # Unit tests for isolated logic
│   │   └── test_task_status.py       # Example: task status transition logic test
│   ├── ui/                           # End-to-end / UI tests using Playwright
│   │   ├── test_login_logout.py      # Login and logout workflow test
│   │   └── test_task_management.py   # Task creation/deletion workflow test
│   └── conftest.py                   # Shared fixtures and test configuration
│
├── evidence/                         # Testing evidence and supporting artifacts
│   ├── screenshots/                  # UI screenshots from manual or automated testing
│   ├── logs/                         # flake8, pylint, and test execution logs
│   ├── accessibility/                # Accessibility scan evidence
│   └── models/                       # State-model diagrams or workflow visuals
│
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions workflow for linting and tests
│
├── .gitignore                        # Files and folders ignored by Git
├── LICENSE                           # Project license
├── README.md                         # Repository overview and setup guide
├── requirements.txt                  # Python package dependencies
├── run.py                            # Application entry point
└── text                              # Existing project text/support file from repository
