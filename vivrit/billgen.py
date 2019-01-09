#!/usr/bin/python

class billGen(object):
	def __init__(self, itemname,mrp,qty,disc,total_price):
		self.itemname = itemname
		self.mrp = mrp
		self.qty = qty
		self.disc = disc
		self.total_price = total_price
