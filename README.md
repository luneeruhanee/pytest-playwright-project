# 🧪 Playwright Automation Testing Project (Python)

This project is an automation testing framework built using Playwright and Pytest with Python.

## 📌 Overview

This project demonstrates end-to-end (E2E) testing for a web application, including:

* UI Automation Testing
* API Integration Testing
* Page Object Model (POM) design pattern
* Data-driven testing using JSON
* BDD testing with pytest-bdd

## 🛠 Tech Stack

* Python
* Playwright
* Pytest
* Pytest-BDD
* HTML Reports

## 📂 Project Structure

```
PytestProject/
│
├── playwright/
│   ├── PageObject/
│   ├── tests/
│   ├── utils/
│   └── data/
│
├── pytestDir/
├── requirements.txt
└── README.md
```

## 🚀 How to Run Tests

### 1. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
playwright install
```

### 3. Run tests

```
pytest
```

### 4. Run specific tests

```
pytest -m smoke
```

## 📊 Test Features

* Login functionality
* Order creation via API
* Order verification via UI
* Network validation tests
* Cross-browser testing

## 📈 Reports

To generate HTML report:

```
pytest --html=report.html
```

## 🔐 Test Data

Test data is stored in JSON format.
Sensitive data is excluded using `.gitignore`.

## 💡 Notes

This project was created as part of learning automation testing using Playwright and Pytest, and demonstrates real-world QA practices.

---

👩‍💻 Author: Ruhanee Tohlee
