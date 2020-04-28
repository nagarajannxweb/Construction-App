from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Construction"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Item Type",
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Rate Analysis",
                    "onboard": 1
                },
            ]
        }
    ]
