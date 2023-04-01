import unittest
from datetime import datetime

import bank_app
from bank_app import (
    delete_transactions,
    insert_transaction,
    search_transactions,
    sort_transactions,
)

SEED_DATA = [
    {
        "date": datetime(2023, 1, 1),
        "description": "Transaction A",
        "amount": 100.0,
        "type": "debit",
    },
    {
        "date": datetime(2023, 1, 2),
        "description": "Transaction B",
        "amount": 200.0,
        "type": "credit",
    },
]


class TestBankApp(unittest.TestCase):
    def setUp(self):
        bank_app.transactions_objects = SEED_DATA[:]

    def reset_seed_data(self):
        bank_app.transactions_objects = SEED_DATA[:]

    def test_insert_transaction(self):
        transaction = {
            "date": datetime(2023, 1, 3),
            "description": "Test transaction",
            "amount": 300.0,
            "type": "debit",
        }
        another_transaction = {
            "date": datetime(2023, 1, 4),
            "description": "Test transaction 2",
            "amount": 100.0,
            "type": "credit",
        }
        # Insert a new transaction
        insert_transaction(transaction)
        # Assert the new transaction is in the list
        self.assertIn(transaction, bank_app.transactions_objects)
        # Assert the total count of transaction is 3 (2 seed objects and the new transaction)
        self.assertEqual(len(bank_app.transactions_objects), 3)

        # Insert another new transaction is in the list
        insert_transaction(another_transaction)
        # Assert the new another_transaction is in the list
        self.assertIn(transaction, bank_app.transactions_objects)
        # Assert the total count of transaction is 4 (2 seed objects and the 2 new transactions)
        self.assertEqual(len(bank_app.transactions_objects), 4)

    def test_delete_transactions(self):
        keyword = "Transaction A"
        # Delete seed transaction
        message = delete_transactions(keyword)
        # Assert we successfully deleted a single transaction
        self.assertEqual(message, "1 transaction(s) successfully deleted.")

        # Reset the seed data to 2 transactions
        self.reset_seed_data()

        # Use a keyword that is present in two different transaction
        keyword = "Transaction"
        message = delete_transactions(keyword)
        # Assert we successfully deleted two transactions
        self.assertEqual(message, "2 transaction(s) successfully deleted.")

    def test_delete_transactions_with_no_transactions(self):
        # Empty the transactions_object list
        bank_app.transactions_objects = []
        keyword = "Transaction A"

        # Assert NoTransactionsError was succesfully raised as the list is empty
        with self.assertRaises(bank_app.NoTransactionsError):
            bank_app.delete_transactions(keyword)

    def test_sort_transactions_asc(self):
        # Sort transactions by amount and asc
        sorted_transactions = sort_transactions("amount")
        # Assert the first amount in the list is the lowest of the two
        self.assertEqual(sorted_transactions[0]["amount"], 100.0)
        # Assert the second amount in the list is the highest of the two
        self.assertEqual(sorted_transactions[1]["amount"], 200.0)

    def test_sort_transactions_desc(self):
        # Sort transactions by amount and desc
        sorted_transactions = sort_transactions("amount", True)

        # Assert the first amount in the list is the highest of the two
        self.assertEqual(sorted_transactions[0]["amount"], 200.0)
        # Assert the second amount in the list is the lowest of the two
        self.assertEqual(sorted_transactions[1]["amount"], 100.0)

    def test_sort_transactions_with_invalid_field_error(self):
        # Assert InvalidFieldError is raised when providing an invalid field value
        with self.assertRaises(bank_app.InvalidFieldError):
            bank_app.sort_transactions("invalid_field", True)

    def test_sort_transactions_when_there_are_no_transactions(self):
        bank_app.transactions_objects = []

        # Assert NoTransactionsError is raised when there are no transactions
        with self.assertRaises(bank_app.NoTransactionsError):
            bank_app.sort_transactions("amount", True)

    def test_search_transactions(self):
        keyword = "Transaction A"
        # Search in transactions with a single matching keyword
        matched_transactions = search_transactions(keyword)

        # Assert only one object matches
        self.assertEqual(len(matched_transactions), 1)
        # Assert "Transaction A" is present in the matched description
        self.assertIn(keyword, matched_transactions[0]["description"])

        # Use a keyword that is present in two different descriptions
        keyword = "Transaction"
        # Search in transactions with the common matching keyword
        matched_transactions = search_transactions(keyword)

        # Assert two objects matched
        self.assertEqual(len(matched_transactions), 2)
        # Assert "Transaction" is present in both descriptions
        self.assertIn(keyword, matched_transactions[0]["description"])
        self.assertIn(keyword, matched_transactions[1]["description"])

    def test_search_transactions_no_match(self):
        keyword = "Not a valid transaction"

        # Assert NoMatchingTransactionsError is raised when no transactions match
        with self.assertRaises(bank_app.NoMatchingTransactionsError):
            search_transactions(keyword)

    def test_search_transactions_when_there_are_no_transactions(self):
        # Empty the transactions objects list
        bank_app.transactions_objects = []
        keyword = "Transaction A"

        # Assert NoTransactionsError is raised when there are no transactions in the list
        with self.assertRaises(bank_app.NoTransactionsError):
            bank_app.search_transactions(keyword)


if __name__ == "__main__":
    unittest.main()
