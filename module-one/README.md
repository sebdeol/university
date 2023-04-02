# README

## Bank Account Book Application

## Introduction

This is the GitHub repository hosting the code for the Bank Account Book application.

The Bank Account Book is a powerful and user-friendly Python application that lets users keep track of their day-to-day transactions.
The application is designed in a simple yet effective way to add, delete, search, and sort all banking transactions in one single place via the terminal.


## Objective

The primary objective of this application is to provide users with an easy way to manage their bank account transactions.
Users can maintain a record of their transactions, keep track of their expenses and incomes.
Users can also quickly search and sort transactions based on specific criterias.

## Implementation

The application is implemented in Python and uses basic data structures like lists and dictionaries to store transaction records.
The key data structures and methods used in the application are:

- Lists: Lists are used to store the transaction records (Python Software Foundation, n.d.a).
- Dictionaries: Each transaction record is stored as a dictionary with keys such as 'date', 'description', 'amount', and 'type' (Python Software Foundation, n.d.b).
- Datetime objects: The transaction dates are stored as datetime objects for easy manipulation and formatting (Python Software Foundation, n.d.c).

The application is divided into several functions, each responsible for a specific operation, such as adding, deleting, searching, and sorting transactions.
This approach ensures that the code is easy to maintain and update in future iterations.

## Data Structures

### Transaction Object

Each transaction object is represented as a dictionary with the following fields:

- date (datetime (Python Software Foundation, n.d.c)): The transaction's date, stored as a datetime object.
- description (string (Python Software Foundation, n.d.d)): A brief description of the transaction.
- amount (float (Python Software Foundation, n.d.e)): The transaction amount, stored as a floating-point number.
- type (string (Python Software Foundation, n.d.d)): The transaction type, which can be either 'debit' or 'credit'.

### Transactions List

The list of transactions is stored as a list of dictionaries, with each dictionary representing a transaction record.

## How to Execute the Code

The application has been developed and tested using Python 3.11 however it should be compatible with Python 3.6 or higher versions.
Ensure that both [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) are installed on your system before proceeding.

### Instructions to execute the Bank Account Book Application

1) Open your preferred terminal application and clone the repository to your local system:

```bash
git clone git@github.com:sebdeol/university.git
```

2) Navigate to the application folder:

```bash
cd university/module-one
```

3) Start the application:
```
python3 bank_app.py
```

4) If you successfully followed the instruction, the application will display a menu with the available operations in your terminal (please note that the application will display a reduced menu until at least a transaction is entered to improve the UX):


```bash
❯ python3 bank_app.py

Bank Account Book Application
1. Add a transaction
6. Exit
Enter your choice:
```

5) Follow the on-screen prompts to perform the desired actions.


If you want to test the application, you can also run the python tests:

```bash
python3 -m unittest test_bank_app.py
```


### Instructions for Use

The Bank Account Book Application provides a text-based interface with a menu of available operations.
Here's a brief overview of the available options:

- Add a transaction: Enter the transaction's date, description, amount, and type (debit or credit). The application will add the transaction to the list of records and display a confirmation message.

- Delete a transaction: Enter a keyword or string to delete for transactions with matching descriptions. The application will then confirm how many transactions were deleted.

- Search transactions: Enter a keyword or string to search for transactions with matching descriptions. The application will display a list of transactions containing the entered keyword or string.

- Sort transactions: Choose a field (date, description, amount) and order (ascending or descending) to sort the list of transactions.
The application will display the sorted list of transactions in a table

- Display all transactions: The application will display all the current transactions in a table.

- Exit: To exit the application.

The application has been designed to minimise user errors. For example, if you enter an invalid value, the app should tell you and prompt you to perform your desired action again.

## References

Python Software Foundation, n.d.a. Lists. [online] Python.org. Available at: https://docs.python.org/3/library/stdtypes.html#lists [Accessed 1 April 2023].

Python Software Foundation, n.d.b. Dictionaries. [online] Python.org. Available at: https://docs.python.org/3/tutorial/datastructures.html#dictionaries [Accessed 1 April 2023].

Python Software Foundation, n.d.c. datetime. [online] Python.org. Available at: https://docs.python.org/3/library/datetime.html [Accessed 1 April 2023].

Python Software Foundation, n.d.d. string. [online] Python.org. Available at: https://docs.python.org/3/library/stdtypes.html#string-methods [Accessed 1 April 2023].

Python Software Foundation, n.d.e. float(). [online] Python.org. Available at: https://docs.python.org/3/library/functions.html#float [Accessed 1 April 2023].
