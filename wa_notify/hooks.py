# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "wa_notify"
app_title = "Frappe Whatsapp Cloud Api Notifications"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Whatsapp Cloud Api Notifications for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/wa_notify/css/wa_notify.bundle.css"
app_include_js = "/assets/wa_notify/js/wa_notify.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "wa_notify.engine.on_document_submit",
        "on_cancel": "wa_notify.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "wa_notify.engine.daily_scheduled_sync"
    ]
}
