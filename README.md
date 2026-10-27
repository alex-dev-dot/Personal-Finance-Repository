# Personal Finance Analyzer

This is my project in Python for tracking personal income and expenses. The program lets you add and delete transactions, view the balance, search for records, and get simple statistics.

The project helped me practice working with functions, lists and dictionaries, JSON files, error handling, sorting, and tests.

## Features

- adding income and expenses;
- viewing transactions sorted by date;
- calculating the total balance;
- statistics on income and expenses;
- displaying the three largest expenses;
- searching by category and description;
- filtering transactions for a period;
- monthly report;
- deleting a transaction by ID;
- saving data between program runs.

## Technologies Used

- **Python** — the main program logic;
- **JSON** — storing transactions;
- **pathlib** — working with file paths;
- **datetime** — handling dates;
- **heapq** — finding large expenses;
- **pytest** — testing;
- **Merge sort** — sorting transactions by date.

No additional libraries are needed for a normal run. `pytest` is installed separately if you need to run the tests.

## Project Structure

```text
Personal_Finance_Analyzer_v2/
├── main.py
├── analytics.py
├── storage.py
├── validators.py
├── test_analytics.py
├── test_validators.py
└── data/
    └── transactions.json
```

Brief overview of the files:

- `main.py` — menu and user interaction;
- `analytics.py` — calculations, search, sorting, and reports;
- `storage.py` — loading and saving data;
- `validators.py` — validating entered values;
- `test_analytics.py` and `test_validators.py` — tests;
- `data/transactions.json` — the file with transactions.

## Installation and Running

You need Python installed. Go to the project folder and run the commands.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Install pytest if you plan to run the tests:
```bash
python -m pip install pytest
```

Run the program:
```bash
python main.py
```

## How to Use the Program

After launching, a menu appears:

1. **Add operation** — add an income or expense.
2. **All operations (by date)** — view all transactions.
3. **Balance** — calculate the balance.
4. **Show stats** — view statistics.
5. **Top expenses** — show the largest expenses.
6. **Top category** — show the categories with the largest amounts.
7. **Search** — find a transaction by category or description.
8. **Operations by period** — display transactions for the selected period.
9. **Monthly report** — view income and expense totals by month.
10. **Delete operation by ID** — delete a transaction by its ID.
0. **Exit** — exit the program.

When adding a transaction, you need to specify the type (`income` or `expense`), amount, category, date, and description. The date is entered in the `YYYY-MM-DD` format.

The balance is calculated using the formula:

```text
Balance = income − expenses
```
Data is saved to data/transactions.json, so it is not lost after the program is closed.

## Data Validation

Before adding a transaction, the program validates the entered values. For example, the amount must be greater than zero, the transaction type must be income or expense, and the date must have the correct format.

If incorrect data is entered, the program reports an error and asks you to enter it again.

## Testing

Tests are run from the project folder with the command:
```bash
python -m pytest -v
```

Analytics tests only:
```bash
python -m pytest -v test_analytics.py
```

Data validation tests only:
```bash
python -m pytest -v test_validators.py
```