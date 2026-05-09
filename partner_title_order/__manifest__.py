# Copyright 2020 Camptocamp SA
# Copyright 2026 NTJ (https://www.ntj.co.id)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# v19-incompat: Removed in v19: model res.partner.title no longer exists.
{
    "name": "Partner title order",
    "summary": "Makes partner title sortable by sequence",
    "version": "19.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "website": "https://github.com/OCA/partner-contact",
    "data": [
        "views/res_partner_title_views.xml",
    ],
    "installable": False,
}
