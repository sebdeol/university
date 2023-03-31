import unittest
from datetime import datetime

import bank_app
from bank_app import (
    InvalidFieldError,
    NoMatchingTransactionsError,
    NoTransactionsError,
    delete_transactions,
    insert_transaction,
    search_transactions,
    sort_transactions,
    transactions_objects,
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

    def test_insert_transaction(self):
        transaction = {
            "date": datetime(2023, 1, 3),
            "description": "Test transaction",
            "amount": 300.0,
            "type": "debit",
        }
        insert_transaction(transaction)

        self.assertIn(transaction, bank_app.transactions_objects)
        self.assertEqual(len(bank_app.transactions_objects), 3)

    def test_delete_transactions(self):
        keyword = "Transaction A"
        message = delete_transactions(keyword)

        self.assertEqual(message, "1 transaction(s) successfully deleted.")

    def test_delete_transactions_with_no_transactions(self):
        bank_app.transactions_objects = []
        keyword = "Transaction A"

        with self.assertRaises(bank_app.NoTransactionsError):
            bank_app.delete_transactions(keyword)

    def test_sort_transactions(self):
        sorted_transactions = sort_transactions("amount")

        self.assertEqual(sorted_transactions[0]["amount"], 100.0)
        self.assertEqual(sorted_transactions[1]["amount"], 200.0)

    def test_sort_transactions_desc(self):
        sorted_transactions = sort_transactions("amount", True)

        self.assertEqual(sorted_transactions[0]["amount"], 200.0)
        self.assertEqual(sorted_transactions[1]["amount"], 100.0)

    def test_sort_transactions_with_invalid_field_error(self):
        with self.assertRaises(bank_app.InvalidFieldError):
            bank_app.sort_transactions("invalid_field", True)

    def test_sort_transactions_when_there_are_no_transactions(self):
        bank_app.transactions_objects = []

        with self.assertRaises(bank_app.NoTransactionsError):
            bank_app.sort_transactions("amount", True)

    def test_search_transactions(self):
        keyword = "Transaction A"
        matched_transactions = search_transactions(keyword)
        keyword = "Transaction A"

        self.assertEqual(len(matched_transactions), 1)
        self.assertEqual(matched_transactions[0]["description"], "Transaction A")

    def test_search_transactions_no_match(self):
        keyword = "Non-existent transaction"

        with self.assertRaises(bank_app.NoMatchingTransactionsError):
            search_transactions(keyword)

    def test_search_transactions_when_there_are_no_transactions(self):
        bank_app.transactions_objects = []
        keyword = "Transaction A"

        with self.assertRaises(bank_app.NoTransactionsError):
            bank_app.search_transactions(keyword)


if __name__ == "__main__":
    unittest.main()
