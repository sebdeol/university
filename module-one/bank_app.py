# Import the sys module to handle system parameters and functions
import sys

# Import the datetime module to work with dates
from datetime import datetime

# A list to store all the transaction objects
transactions_objects = []

# A constant string for the error message when there are no transactions
NO_TRANSACTIONS_ERROR_MESSAGE = (
    "There is no current transactions. Please add one before performing this action."
)

# Function to insert a transaction into the transactions_objects list
def insert_transaction(transaction):
    # Append the dict object to the transaction list
    transactions_objects.append(transaction)

    # Return a string
    return "Transaction successfully created."


# Function to delete transactions based on a keyword match in their description
def delete_transactions(keyword):
    # Return the no transactions error message if the transactions list is empty
    if not transactions_objects:
        return NO_TRANSACTIONS_ERROR_MESSAGE

    # Initialise an empty list to store the number of deleted transactions
    deleted_count = 0

    # Iterate over a copy of transactions_objects to prevent issues while modifying the list during the iteration
    for transaction in transactions_objects[:]:
        # Compare the lowercase keyword with the lowercase description to make sure we get a match
        if keyword.lower() in transaction["description"].lower():
            # Remove the object from the transactions list
            transactions_objects.remove(transaction)
            # Bump the deleted objects count
            deleted_count += 1

    # If an object was deleted return this string
    if deleted_count > 0:
        return f"{deleted_count} transaction(s) successfully deleted."

    # If no object was deleted return this string
    return "No matching transactions found, nothing was deleted. Please try again with another keyword."


# Function to sort transactions based on the given field and order
def sort_transactions(field, order=False):
    # Return the no transactions error message if the transactions list is empty
    if not transactions_objects:
        return NO_TRANSACTIONS_ERROR_MESSAGE

    # Check if the input field to sort on is valid
    if field not in ("date", "description", "amount"):
        return False, "You provided an invalid field to sort on, please try again.", []

    # Return this tuple with the sorted transactions using the lambda function as the sorting key
    return True, "", sorted(transactions_objects, key=lambda x: x[field], reverse=order)


# Function to search transactions based on a keyword match in their description
def search_transactions(keyword):
    # Return the no transactions error message if the transactions list is empty
    if not transactions_objects:
        return False, [], NO_TRANSACTIONS_ERROR_MESSAGE

    # Initialise an empty list to store the matched transactions
    matched_transactions = []

    # Iterate over each transaction in the transactions_objects
    for transaction in transactions_objects:
        # Compare the lowercase keyword with the lowercase description to make sure we get a match
        if keyword.lower() in transaction["description"].lower():
            # If there's a match, add the transaction to the matched_transactions list
            matched_transactions.append(transaction)

    # Check if there are any matched transactions
    if matched_transactions:
        # If there are matched transactions, return True, the list of matched transactions, and a success message
        return True, matched_transactions, "Matched Transactions: \n"

    # If there was no matched transactions, return False, an empty list, and a message indicating that no transactions were found
    return False, [], "No transactions found, please try again."


# Function to display the transactions in a formatted table
def display_transactions(transactions):
    # Return the no transactions error message if the transactions list is empty
    if not transactions:
        return NO_TRANSACTIONS_ERROR_MESSAGE

    try:
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

    # Handle the TypeError exception if there's an issue with the provided input
    except TypeError:
        print("You entered an invalid value. Please try again.")


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

    # Return the transaction details as a dictionary
    return {
        "date": date,
        "description": description,
        "amount": amount,
        "type": transaction_type,
    }


# Main function to run the bank account book application
def main():
    try:
        # Start an infinite loop for user interaction
        while True:
            # Initialise the choice variable to store the user's menu selection
            choice = 0

            # Print the main menu options
            print("\nBank Account Book Application")
            print("1. Add a transaction")
            print("2. Delete transactions")
            print("3. Sort transactions")
            print("4. Search transactions")
            print("5. Display all transactions")
            print("6. Exit")

            # Prompt the user to enter their menu choice
            # Handle ValueError if the input is not an integer
            try:
                choice = int(input("Enter your choice: \n"))
            except ValueError:
                pass

            # Check if the user's choice is 1 (Add a transaction)
            if choice == 1:
                try:
                    # Prompt the user to enter transaction details
                    transaction = prompt_transaction()
                    # Add the transaction to the list
                    message = insert_transaction(transaction)
                except ValueError:
                    # Handle ValueError if the user entered an invalid value for the transaction details
                    message = (
                        " \nIt appears you entered an invalid value. Please try again."
                    )
                # Display the result message
                print(message)

            # Check if the user's choice is 2 (Delete transactions)
            elif choice == 2:
                # Prompt the user to enter a keyword
                keyword = input("Enter a keyword to delete the matching transactions: ")

                # Delete the matching transactions given the keyword
                message = delete_transactions(keyword)

                # Display the result message
                print(message)

            # Check if the user's choice is 3 (Sort transactions)
            elif choice == 3:
                # Prompt the user to enter the sorting field
                field = input("Enter the field to sort by (date/description/amount): ")

                # Prompt the user to enter the sorting order
                order = input("Enter the order asc/desc (current default is asc): ")
                reverse_order = True if order == "desc" else False

                # Run the sort_transactions() function to sort the transactions according to the input params
                valid_output, message, sorted_transactions = sort_transactions(
                    field, reverse_order
                )

                # Check if the output is valid
                if valid_output:
                    # Display the sorted transactions
                    display_transactions(sorted_transactions)
                else:
                    # Display an error message if the sorting parameters were invalid
                    print(message)

            # Check if the user's choice is 4 (Search transactions)
            elif choice == 4:
                # Prompt the user to enter a keyword
                keyword = input("Enter a keyword to search transactions: ")

                # Search for the matching transactions
                valid_output, matched_transactions, message = search_transactions(
                    keyword
                )

                # Check if the output is valid
                if valid_output:
                    # Display the search result message
                    print(message)

                    # Display the matched transactions
                    display_transactions(matched_transactions)
                else:
                    # Display the error message if no transactions were found
                    print(message)

            # Check if the user's choice is 5 (Display all transactions)
            elif choice == 5:
                # Display all the transactions in the transactions_objects list
                display_transactions(transactions_objects)

            # Check if the user's choice is 6 (Exit)
            elif choice == 6:
                # Print the exit message
                print("Exiting the application.")

                # break the infinite loop to exit the application
                break

            # Handle the case when the user selects an invalid choice
            else:
                print("Invalid choice selected. Please try again.")

    # Handle KeyboardInterrupt to exit the application more gracefully
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
