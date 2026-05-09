# Copyright 2024 Camptocamp SA
# Copyright 2026 NTJ (https://www.ntj.co.id)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# v19-incompat: Removed in v19: model res.partner.title no longer exists.
{
    "name": "Partner Title Active",
    "version": "19.0.1.0.0",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Contact",
    "depends": [
        # Odoo/core
        "base",
    ],
    "website": "https://github.com/OCA/partner-contact",
    "data": [
        "views/res_partner_title.xml",
    ],
    "installable": False,
}
