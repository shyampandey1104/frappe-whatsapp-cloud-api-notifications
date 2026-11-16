import unittest
from wa_notify.engine import WhatsAppCloudAPIEngine

class TestWhatsAppCloudAPI(unittest.TestCase):
    def test_invoice_delivery_payload(self):
        engine = WhatsAppCloudAPIEngine()

        template = engine.format_invoice_notification(
            customer_mobile="+91-98200-11223",
            customer_name="Sunil Mittal",
            invoice_number="INV-2026-004",
            invoice_amount=15400.0,
            pdf_download_url="https://erp.enterprise.com/invoices/INV-2026-004.pdf",
            quick_pay_link="https://rzp.io/l/inv004"
        )
        self.assertEqual(template.recipient_mobile_with_country_code, "919820011223")
        self.assertEqual(template.template_name, "sales_invoice_delivery_v2")

        res = engine.dispatch_message(template)
        self.assertEqual(res.status, "DISPATCHED")
        self.assertTrue(res.message_id.startswith("wamid."))
        self.assertIn("INV-2026-004", res.payload_json)

if __name__ == "__main__":
    unittest.main()
