# Cricbuzz Live Cricket Score Bot

## Project Overview
This project uses Python and Playwright to capture cricket scores from the Cricbuzz website.

The bot opens Cricbuzz, waits for the score element to appear, prints the score in the terminal, and saves a screenshot.

## Technologies Used
- Python
- Playwright
- Chromium
- VS Code

## Project Structure
```text
cricket-score/
├── venv/
├── cricbuzz_score.py
├── score.png
├── headless_debug.png
├── README.md
└── requirements.txt
```

## Installation

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install Playwright:

```bash
pip install playwright
```

3. Install Chromium:

```bash
playwright install chromium
```

## How to Run

Execute the following command:

```bash
python cricbuzz_score.py
```

## Features
- Opens Cricbuzz using Playwright.
- Uses a CSS selector to locate cricket scores.
- Waits for the score element using `wait_for_selector()`.
- Prints the score in the terminal.
- Saves a screenshot as `score.png`.
- Handles timeout errors.

## Sample Output

```text
Opening Cricbuzz...
Waiting for cricket scores...

Latest cricket score:
143-5 (22.4)

Screenshot saved as score.png
```

*Note: The displayed score is an example from the test run and may change.*

## Browser Testing
- Headed mode: Successfully tested.
- Headless mode: Tested, but Cricbuzz returned an Access Denied response.

## Author
Python Playwright Assignment – Week 1, Day 3, Task 1
