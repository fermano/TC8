import unittest

from src.ticket_workflow_seed import DEFAULT_SOURCE, delivery_summary


class DeliverySummarySourceTests(unittest.TestCase):
    def test_default_output_excludes_source(self):
        self.assertEqual(
            delivery_summary({"owner": "Billing-Ops", "status": "queued"}),
            {"owner": "billing-ops", "status": "queued"},
        )

    def test_include_source_with_value(self):
        summary = delivery_summary(
            {"owner": "billing-ops", "status": "sent", "source": " Webhook "},
            include_source=True,
        )
        self.assertEqual(summary["source"], "webhook")

    def test_include_source_blank_defaults_to_unspecified(self):
        summary = delivery_summary(
            {"owner": "billing-ops", "status": "sent", "source": "  "},
            include_source=True,
        )
        self.assertEqual(summary["source"], DEFAULT_SOURCE)

    def test_include_source_missing_defaults_to_unspecified(self):
        summary = delivery_summary(
            {"owner": "billing-ops", "status": "sent"},
            include_source=True,
        )
        self.assertEqual(summary["source"], "unspecified")


if __name__ == "__main__":
    unittest.main()
