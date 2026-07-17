# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Commission + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_commission",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/commission.xml",
        "security/res_group/marketing_commission.xml",
        "security/ir_rule/commission.xml",
        "security/ir_rule/marketing_commission.xml",
        "view/commission.xml",
        "view/marketing_commission.xml",
    ],
}
