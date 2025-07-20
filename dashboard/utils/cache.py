import frappe
from frappe.website.utils import clear_cache

def clear_dashboard_cache(doc=None, method=None):
    # Clear the cache for the specific "/dashboard" route
    clear_cache("/dashboard")

    # Optionally clear general site cache as well
    frappe.clear_cache()
