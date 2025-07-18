import frappe

def get_context(context):
    user = frappe.session.user
    user_roles = frappe.get_roles(user)

    icons = frappe.get_all("Dashboard Icon", fields=["label", "icon", "url", "role"])
    visible_icons = []

    for icon in icons:
        if not icon.role or icon.role in user_roles:
            visible_icons.append(icon)

    context.icons = visible_icons
    return context
