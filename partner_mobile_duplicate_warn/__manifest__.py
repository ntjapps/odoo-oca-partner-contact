# Copyright 2021-2022 Akretion France (http://www.akretion.com/)
# Copyright 2026 NTJ (https://www.ntj.co.id)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# v19-incompat: Removed in v19: res.partner.mobile field consolidated into phone.
{
    "name": "Partner Mobile Duplicate Warn",
    "version": "19.0.1.0.0",
    "category": "Partner Management",
    "license": "AGPL-3",
    "summary": "Warning banner on partner form if another partner has the same mobile",
    "author": "Akretion,Odoo Community Association (OCA)",
    "maintainers": ["alexis-via"],
    "website": "https://github.com/OCA/partner-contact",
    "depends": ["phone_validation"],
    # I add phonenumbers in external_dependencies
    # because the phone_validation module doesn't do it
    # and it's needed for Travis
    "external_dependencies": {"python": ["phonenumbers"]},
    "data": [
        "views/res_partner.xml",
    ],
    "installable": False,
}
