# Import the sys module to handle system parameters and functions
import sys

# Import the datetime module to work with dates
from datetime import datetime

# A list to store all the transaction objects
transactions_objects = []

# A list with 5 pre-populated objects
# Uncomment the lines below if you don't want to manually create the objects when you start the app.

# transactions_objects = [
#     {
#         "date": datetime.strptime("2023-03-01", "%Y-%m-%d"),
#         "description": "Shopping",
#         "amount": 50.00,
#         "type": "debit",
#     },
#     {
#         "date": datetime.strptime("2023-03-02", "%Y-%m-%d"),
#         "description": "Another Shopping",
#         "amount": 20.00,
#         "type": "debit",
#     },
#     {
#         "date": datetime.strptime("2023-03-03", "%Y-%m-%d"),
#         "description": "Salary",
#         "amount": 2000.00,
#         "type": "credit",
#     },
#     {
#         "date": datetime.strptime("2023-03-04", "%Y-%m-%d"),
#         "description": "ASOS",
#         "amount": 220.11,
#         "type": "debit",
#     },
#     {
#         "date": datetime.strptime("2023-03-05", "%Y-%m-%d"),
#         "description": "Restaurant",
#         "amount": 76.99,
#         "type": "debit",
#     },
# ]

# A constant string for the error message when there are no transactions
NO_TRANSACTIONS_ERROR_MESSAGE = (
    "There are no current transactions. Please add one before performing this action."
)

# Custom exceptions errors classes
class InvalidFieldError(Exception):
    pass


class NoTransactionsError(Exception):
    pass


class NoMatchingTransactionsError(Exception):
    pass


# Function to insert a transaction into the transactions_objects list
def insert_transaction(transaction):
    # Append the dict object to the transaction list
    transactions_objects.append(transaction)
    return "Transaction successfully created."


# Function to delete transactions based on a keyword match in their description
def delete_transactions(keyword):
    # Check if there are transactions otherwise raise NoTransactionsError
    if not transactions_objects:
        raise NoTransactionsError(NO_TRANSACTIONS_ERROR_MESSAGE)

    # Initialise an empty list to store the number of deleted transactions
    deleted_count = 0

    # Iterate over a copy of transactions_objects to prevent issues while modifying the list during the iteration
    for transaction in transactions_objects[:]:
        # Compare the lowercase keyword with the lowercase description to make sure we get a match
        if keyword.lower() in transaction["description"].lower():
            # Remove the object from the transactions list
            transactions_objects.remove(transaction)
            # Increment the deleted objects count
            deleted_count += 1

    # Check if any transactions were deleted otherwise raise NoMatchingTransactionsError
    if deleted_count == 0:
        raise NoMatchingTransactionsError(
            "No matching transactions found, nothing was deleted. Please try again with another keyword."
        )

    # Return a message indicating the number of deleted transactions
    return f"{deleted_count} transaction(s) successfully deleted."


# Function to sort transactions based on the given field and order
def sort_transactions(field, ascending=False):
    # Check if there are transactions otherwise raise NoTransactionsError
    if not transactions_objects:
        raise NoTransactionsError(NO_TRANSACTIONS_ERROR_MESSAGE)

    # Check if the input field to sort on is valid otherwise raise InvalidFieldError
    if field not in ("date", "description", "amount"):
        raise InvalidFieldError(
            "You provided an invalid field to sort on, please try again."
        )

    # Return the sorted transactions using the lambda function as the sorting key
    return sorted(transactions_objects, key=lambda x: x[field], reverse=ascending)


# Function to search transactions based on a keyword match in their description
def search_transactions(keyword):
    # Check if there are transactions
    if not transactions_objects:
        # Raise NoTransactionsError if there are no transactions
        raise NoTransactionsError(NO_TRANSACTIONS_ERROR_MESSAGE)

    # Initialise an empty list to store the matched transactions
    matched_transactions = []

    # Iterate over each transaction in the transactions_objects
    for transaction in transactions_objects:
        # Compare the lowercase keyword with the lowercase description to make sure we get a match
        if keyword.lower() in transaction["description"].lower():
            # If there's a match, add the transaction to the matched_transactions list
            matched_transactions.append(transaction)

    # Check if there are any matched transactions otherwise raise NoMatchingTransactionsError
    if not matched_transactions:
        raise NoMatchingTransactionsError("No transactions found, please try again.")

    return matched_transactions


# Function to display the transactions in a formatted table
def display_transactions(transactions):
    # Check if there are transactions otherwise raise NoTransactionsError
    if not transactions:
        raise NoTransactionsError(NO_TRANSACTIONS_ERROR_MESSAGE)

    # Print the table header with specifically formatted column names
    print(f"{'ID':<5} {'Date':<12} {'Description':<40} {'Amount':<15} {'Type':<10}")

    # Print a separator line for better readability
    print("-" * 82)

    # Iterate over each transaction in the transactions list
    for idx, record in enumerate(transactions):
        # Extract and format the transaction details for display
        date = record["date"].strftime("%Y-%m-%d")
        description = record["description"]
        amount = record["amount"]
        transaction_type = record["type"]

        # Print the transaction details in a formatted row
        print(
            f"{idx:<5} {date:<12} {description:<40} {amount:<15.2f} {transaction_type:<10}"
        )


# Function to prompt the user for the transaction details and return a dictionary
def prompt_transaction():
    # Prompt the user to enter the transaction date and convert it to a datetime object
    date_str = input("Enter the date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # Prompt the user to enter the transaction description
    description = input("Enter the description: ")

    # Prompt the user to enter the transaction amount and convert it to a float
    amount = float(input("Enter the amount: "))

    # Prompt the user to enter the transaction type (debit or credit)
    transaction_type = input("Enter the transaction type (debit/credit): ")

    # Check if the transaction type is valid otherwise raise ValueError
    if transaction_type.lower() not in ("debit", "credit"):
        raise ValueError("Invalid transaction type entered. Please try again.")

    # Return the transaction details as a dictionary
    return {
        "date": date,
        "description": description,
        "amount": amount,
        "type": transaction_type,
    }


def main():
    try:
        while True:
            choice = 0
            print("\nBank Account Book Application")
            print("1. Add a transaction")

            # Only display an enhanced menu if there is at least one transaction present.
            if transactions_objects:
                print("2. Delete transactions")
                print("3. Sort transactions")
                print("4. Search transactions")
                print("5. Display all transactions")

            print("6. Exit")

            # Prompt the user to enter their menu choice
            # Handle ValueError if the input is not an integer
            try:
                choice = int(input("Enter your choice: \n"))
                # If the transactions list is empty and the user chose an invalid integer raise ValueError
                if not transactions_objects and choice not in (1, 6):
                    choice = 0
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a valid choice.")
                continue

            try:
                # Check if the user's choice is 1 (Add a transaction)
                if choice == 1:
                    # Prompt the user to enter transaction details
                    transaction = prompt_transaction()
                    message = insert_transaction(transaction)
                    print(f"{message}\n")
                    display_transactions(transactions_objects)
                # Check if the user's choice is 2 (Delete transactions)
                elif choice == 2:
                    # Prompt the user to enter a keyword
                    keyword = input(
                        "Enter a keyword to delete the matching transactions: "
                    )
                    message = delete_transactions(keyword)
                    print(f"{message}\n")
                    display_transactions(transactions_objects)
                # Check if the user's choice is 3 (Sort transactions)
                elif choice == 3:
                    # Prompt the user to enter the sorting field
                    field = input(
                        "Enter the field to sort by (date/description/amount): "
                    )
                    # Prompt the user to enter the sorting order
                    order = input("Enter the order asc/desc (current default is asc): ")
                    reverse_order = True if order == "desc" else False
                    sorted_transactions = sort_transactions(field, reverse_order)
                    display_transactions(sorted_transactions)
                # Check if the user's choice is 4 (Search transactions)
                elif choice == 4:
                    # Prompt the user to enter a keyword
                    keyword = input("Enter a keyword to search transactions: ")
                    matched_transactions = search_transactions(keyword)
                    print("Matched Transactions: \n")
                    display_transactions(matched_transactions)
                # Check if the user's choice is 5 (Display all transactions)
                elif choice == 5:
                    display_transactions(transactions_objects)
                # Check if the user's choice is 6 (Exit)
                elif choice == 6:
                    print("Exiting the application. Goodbye!")
                    # Break the infinite loop to exit the application
                    break
                else:
                    raise ValueError
            # Handle ValueError if the user entered an invalid value
            except ValueError:
                print("\nIt appears you entered an invalid value. Please try again.")
            # Handle InvalidFieldError if the user entered an invalid field
            except InvalidFieldError as invalid_field_error:
                print(invalid_field_error)
            # Handle NoMatchingTransactionsError if there are no maching transactions
            except NoMatchingTransactionsError as no_matching_transaction_error:
                print(no_matching_transaction_error)
            # Handle NoTransactionsError if there are no transactions
            except NoTransactionsError as no_transactions_error:
                print(no_transactions_error)

    # Handle KeyboardInterrupt to exit the application more gracefully
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
