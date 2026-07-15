import unittest

from src.ticket_workflow_seed import filter_records_by_owner


class FilterRecordsByOwnerTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"owner": "Billing-Ops", "status": "queued"},
            {"owner": "platform-ops", "status": "sent"},
            {"owner": " billing-ops ", "status": "failed"},
        ]

    def test_missing_selection_returns_all_in_order(self):
        self.assertEqual(filter_records_by_owner(self.records), self.records)

    def test_selection_returns_matching_records_in_order(self):
        result = filter_records_by_owner(self.records, "billing-ops")
        self.assertEqual(result, [self.records[0], self.records[2]])

    def test_selection_is_normalized(self):
        result = filter_records_by_owner(self.records, "  Platform-OPS ")
        self.assertEqual(result, [self.records[1]])


if __name__ == "__main__":
    unittest.main()
