import unittest
from datetime import datetime

from bank_app import (
    NO_TRANSACTIONS_ERROR_MESSAGE,
    delete_transactions,
    insert_transaction,
    search_transactions,
    sort_transactions,
    transactions_objects,
)


class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.sample_transaction = {
            "date": datetime(2023, 3, 17),
            "description": "Groceries",
            "amount": 42.50,
            "type": "debit",
        }
        transactions_objects.clear()

    def tearDown(self) -> None:
        transactions_objects.clear()

    def test_insert_transaction(self):
        self.assertEqual(len(transactions_objects), 0)
        result = insert_transaction(self.sample_transaction)
        self.assertEqual(result, "Transaction successfully created.")
        self.assertEqual(len(transactions_objects), 1)
        self.assertEqual(transactions_objects[0], self.sample_transaction)

    def test_delete_transactions_no_transactions(self):
        result = delete_transactions("Groceries")
        self.assertEqual(result, NO_TRANSACTIONS_ERROR_MESSAGE)

    def test_delete_transactions_no_matching_keyword(self):
        insert_transaction(self.sample_transaction)
        result = delete_transactions("Non-existent")
        self.assertEqual(
            result,
            "No matching transactions found, nothing was deleted. Please try again with another keyword.",
        )

    def test_delete_one_transaction_with_a_matching_keyword(self):
        insert_transaction(self.sample_transaction)
        result = delete_transactions("Groceries")
        self.assertEqual(result, "1 transaction(s) successfully deleted.")
        self.assertEqual(len(transactions_objects), 0)

    def test_delete_two_transactions_with_a_matching_keyword(self):
        another_transaction = {
            "date": datetime(2022, 3, 18),
            "description": "Another Groceries Transaction",
            "amount": 12.00,
            "type": "debit",
        }

        insert_transaction(self.sample_transaction)
        insert_transaction(another_transaction)

        result = delete_transactions("Groceries")

        self.assertEqual(result, "2 transaction(s) successfully deleted.")
        self.assertEqual(len(transactions_objects), 0)

    def test_sort_transactions_no_transactions(self):
        result = sort_transactions("date")
        self.assertEqual(result, NO_TRANSACTIONS_ERROR_MESSAGE)

    def test_sort_transactions_invalid_field(self):
        insert_transaction(self.sample_transaction)

        valid_output, message, sorted_transactions = sort_transactions("invalid")

        self.assertFalse(valid_output)
        self.assertEqual(
            message, "You provided an invalid field to sort on, please try again."
        )
        self.assertEqual(sorted_transactions, [])

    def test_sort_transactions_valid_field(self):
        another_transaction = {
            "date": datetime(2023, 3, 18),
            "description": "Salary",
            "amount": 2000.00,
            "type": "credit",
        }

        insert_transaction(self.sample_transaction)
        insert_transaction(another_transaction)

        valid_output, message, sorted_transactions = sort_transactions("date")

        self.assertTrue(valid_output)
        self.assertEqual(message, "")
        self.assertEqual(
            sorted_transactions, [self.sample_transaction, another_transaction]
        )

    def test_search_transactions_no_transactions(self):
        valid_output, found_transactions, message = search_transactions("Groceries")

        self.assertFalse(valid_output)
        self.assertEqual(found_transactions, [])
        self.assertEqual(message, NO_TRANSACTIONS_ERROR_MESSAGE)

    def test_search_transactions_no_matching_keyword(self):
        insert_transaction(self.sample_transaction)

        valid_output, found_transactions, message = search_transactions("Non-existent")

        self.assertFalse(valid_output)
        self.assertEqual(found_transactions, [])
        self.assertEqual(message, "No transactions found, please try again.")

    def test_search_transactions_matching_keyword(self):
        insert_transaction(self.sample_transaction)
        valid_output, found_transactions, message = search_transactions("Groceries")

        self.assertTrue(valid_output)
        self.assertEqual(len(found_transactions), 1)
        self.assertEqual(found_transactions[0], self.sample_transaction)


if __name__ == "__main__":
    unittest.main()
