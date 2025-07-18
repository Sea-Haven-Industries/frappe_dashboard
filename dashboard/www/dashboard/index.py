import frappe

def get_context(context):
    user = frappe.session.user
    context.roles = frappe.get_roles(user)
    return context
