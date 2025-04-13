
# 💰 Simple Banking System (Python CLI)

This project is a **simple banking system** made in Python, running in the terminal (command-line interface). It allows users to make deposits, withdrawals, check the bank statement, and exit the program through an interactive menu.

## 📋 Features

- [x] Deposit of positive values
- [x] Withdrawals with:
  - Limit per withdrawal ($500)
  - Daily limit of 3 withdrawals
  - Balance check
- [x] Bank statement showing transaction history
- [x] Program exit option `[0]`

## 📌 Business Rules

- Withdrawals cannot exceed the current balance
- The maximum amount per withdrawal is **$500**
- Only **3 withdrawals** are allowed per run
- Negative or zero values are not accepted

## 🧪 Example Usage

```
[1] Deposit
[2] Withdrawal
[3] Bank Statement
[0] Quit

=> 1
Deposit amount: 100

=> 2
Withdrawal amount: 50

=> 3

====== BANK STATEMENT ======
Deposit: $ 100.00
Withdrawal: $ 50.00

Balance: $ 50.00
=============================
```

## 🚀 How to Run

1. Make sure you have [Python 3](https://www.python.org/) installed
2. Save the code to a `.py` file (e.g., `bank_system.py`)
3. In the terminal, run:

```bash
python bank_system.py
```

---

Made with 💙 using Python.
