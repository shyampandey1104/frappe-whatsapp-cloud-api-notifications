# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "wa_notify"
app_title = "Frappe Whatsapp Cloud Api Notifications"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Whatsapp Cloud Api Notifications - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/wa_notify/css/wa_notify.bundle.css"
app_include_js = "/assets/wa_notify/js/wa_notify.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Whatsapp Cloud Api Notifications Entry": {
        "validate": "wa_notify.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "wa_notify.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "wa_notify.tasks.hourly_sync"
    ],
    "daily": [
        "wa_notify.tasks.daily_reconciliation"
    ],
    "weekly": [
        "wa_notify.tasks.weekly_digest"
    ]
}
