// Copyright (c) 2020, nxweb and contributors
// For license information, please see license.txt

{% include 'erpnext/selling/sales_common.js' %}

frappe.ui.form.on("Rate Analysis",{
 refresh:function(frm){
    frm.set_query("item_of_work", function(doc){
        return {
            "filters": {
                "item_type" : "Item of Work"
            }
        };
    });
    frm.fields_dict.rate_analysis_detail.grid.get_field('item_code').get_query = function(frm,cdt,cdn) {
        var child = locals[cdt][cdn];
    		return {
    				filters: {
    					"item_type" : child.item_type
    				}
    		};
    };
  }
});
frappe.ui.form.on("Rate Analysis Detail",{
    rate:function(frm,cdt,cdn){
    var child = locals[cdt][cdn];
    child.amount = child.qty * child.rate
  }
});

//cur_frm.add_fetch("taxes_and_charges","taxes","currency")
