# Copyright (c) 2025, Adam Moussa and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.utils import clear_cache


class DashboardIcon(Document):
	def validate(self):
		clear_cache("/dashboard")
