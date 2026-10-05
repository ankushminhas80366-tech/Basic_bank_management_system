# Basic Bank Management System

A simple console-based **Bank Management System** built with Python and Object-Oriented Programming (OOP).  
This project simulates basic banking operations such as creating accounts, checking details, depositing, and withdrawing money.

---

## Features

- **Create a new account** – Add a new customer with name, account number, and initial balance
- **View account details** – Login and see account holder name, balance, and account number
- **Withdraw / Debit money** – Deduct amount from the account (with balance validation)
- **Deposit / Credit money** – Add money to the account
- **Feedback system** – Submit satisfaction feedback (Very Satisfied / Satisfied / Not Satisfied)
- **Simple authentication** – Name-based password check with limited attempts (3 tries)
- **Input validation** – Handles invalid inputs and common errors gracefully
- **Pre-loaded accounts** – Comes with two sample accounts for quick testing:
  - Ankush (Account: `123456`, Balance: ₹10,000)
  - Rohit (Account: `789012`, Balance: ₹20,000)

---

## Technologies Used

- **Python 3**
- **Object-Oriented Programming (OOP)** – `Axis_Bank` class
- Standard library only (`time` for delays)

---

## Project Structure

```
Basic_bank_management_system/
├── main.py          # Main application file containing the Axis_Bank class and menu loop
└── README.md        # Project documentation
```

---

## How to Run

1. Make sure **Python 3** is installed on your system.
2. Clone or download this repository:
   ```bash
   git clone https://github.com/ankushminhas80366-tech/Basic_bank_management_system.git
   cd Basic_bank_management_system
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Follow the on-screen menu:
   - Press any key to continue
   - Choose an option (1–5)
   - Press `q` to quit

---

## Menu Options

| Option | Action                      |
|--------|-----------------------------|
| 1      | Create a new account        |
| 2      | Check bank details          |
| 3      | Debit / Withdraw money      |
| 4      | Credit / Deposit money      |
| 5      | Give feedback               |
| q      | Quit the application        |

---

## Sample Usage

```
Welcome to Axis Bank:

1: 'For create an account'
2: 'For check your bank details'
3: 'For Debit/Withdrawl money'
4: 'For Credit/Deposit money in your account'
5: 'For Feedback'
```

**Login tip:** When prompted for password, enter the account holder's **name** (e.g., `Ankush` or `Rohit`).

---

## Future Improvements (Ideas)

- Persistent data storage (file or database)
- Multiple transactions history
- Better security (hashed passwords / PIN)
- Transfer money between accounts
- Admin panel to view all accounts
- GUI version using Tkinter or a web framework

---

## Author

**Ankush Minhas**  
GitHub: [ankushminhas80366-tech](https://github.com/ankushminhas80366-tech)

---

## License

This project is open source and available under the [MIT License](LICENSE) (feel free to use and modify).
