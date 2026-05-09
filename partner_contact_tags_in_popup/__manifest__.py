# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
# Copyright 2026 NTJ (https://www.ntj.co.id)
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# v19-incompat: Removed in v19: parent partner form no longer has the mobile field anchor.
{
    "name": "Partner Contact Tags in Contacts & Addresses Pop-up",
    "summary": "Display a contact's tags in the 'Contacts & Addresses' "
    "pop-up form view.",
    "version": "19.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://github.com/OCA/partner-contact",
    "author": "Coop IT Easy SC, Odoo Community Association (OCA)",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "views/res_partner_views.xml",
    ],    "installable": False,
}