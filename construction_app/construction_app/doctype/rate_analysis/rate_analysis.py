# -*- coding: utf-8 -*-
# Copyright (c) 2020, nxweb and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RateAnalysis(Document):
	def validate(self):
		self.calculate_net_total()

	def calculate_net_total(self):
		self.net_total = 0
		for d in self.rate_analysis_detail:
			self.net_total += d.amount
