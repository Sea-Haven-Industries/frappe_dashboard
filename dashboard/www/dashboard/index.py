# Copyright (c) 2025, Adam Moussa and contributors
# For license information, please see license.txt

import frappe

no_cache = 1


def get_context(context):
	user = frappe.session.user
	user_roles = frappe.get_roles(user)

	icons = frappe.get_all("Dashboard Icon", fields=["label", "icon", "url", "role"])
	print(icons)
	visible_icons = []

	for icon in icons:
		if not icon.role or icon.role in user_roles:
			visible_icons.append(icon)

	context.icons = visible_icons
	return context
