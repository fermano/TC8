import unittest

from src.ticket_workflow_seed import DEFAULT_OWNER, normalize_delivery_owner


class OwnerWhitespaceTests(unittest.TestCase):
    def test_internal_whitespace_is_collapsed(self):
        self.assertEqual(normalize_delivery_owner(" Billing   Ops "), "billing ops")

    def test_matches_tc8_service_normalization(self):
        from src.tc8_service import normalize_owner

        self.assertEqual(
            normalize_delivery_owner(" Engineering   Ops "),
            normalize_owner(" Engineering   Ops "),
        )

    def test_blank_owner_uses_default(self):
        self.assertEqual(normalize_delivery_owner("   "), DEFAULT_OWNER)


if __name__ == "__main__":
    unittest.main()
