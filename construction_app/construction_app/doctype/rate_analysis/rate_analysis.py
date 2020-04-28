# -*- coding: utf-8 -*-
# Copyright (c) 2020, nxweb and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from erpnext.controllers.taxes_and_totals import calculate_taxes_and_totals


class RateAnalysis(Document):
	def validate(self):
		self.calculate_net_total()

	def before_save(self):
		self.calculate_taxes_and_charges()

	def calculate_net_total(self):
		self.net_total = 0
		for d in self.rate_analysis_detail:
			self.net_total += d.amount
		self.total = self.net_total
		self.base_total = self.net_total
		self.base_net_total = self.net_total

	def calculate_taxes_and_charges(self):
		if self.taxes_and_charges:
			taxes_doc = frappe.get_doc("Sales Taxes and Charges Template",self.taxes_and_charges)
			self.taxes = taxes_doc.taxes
			amount = 0
			for d in self.taxes:
				d.tax_amount = self.total * (d.rate/100)
				amount += d.tax_amount
				d.total = amount
				self.total_taxes_and_charges += d.tax_amount
				self.grand_total = self.total_taxes_and_charges + self.total
				self.base_grand_total = self.grand_total
				self.rounded_total = self.grand_total
				self.base_rounded_total = self.grand_total
				self.base_total_taxes_and_charges = self.total_taxes_and_charges
