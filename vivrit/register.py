#!/usr/bin/python
import datetime
import customer
import db_handler
# get information on date, customer type
# get items to checkout and apply discount
# generate bill
# update salesdb

class fac_customer:
	def __init(self,age,id):
		if age < 60:
			return customer(age,id)
		if id > 1499 and id < 2001 :
			return employeeCustomer(age,id)
		if age >= 60 and id < 1500 and id > 2001:
			return srCitizen(age,id)
			
class register:

	def __init(self,date,age,id,disc_sr,disc_emp):
		self.__dbConnHandle = NULL
		self.__billstart = 22030
		self.customerObj = fac_customer(age,id)
		self.customerType = type(self.customerObj)

		self.srCitizenDiscount = disc_sr
		self.employeeDiscount = disc_emp

		self.cartitems = ''
		self.bill = ''
		self.totalsales = 0
		
	def checkoutItems(self,aItemId,aQty):	
		#	get itemid from db
		# 	apply discounts based on customer type
		#	add to totalsales section
		# 	add to checkedout item
		#	display appended checkedout items
		if(!self.__dbConnHandle):
			self.__dbConnHandle = dbHandler.getDBConnHandle()	
		
		cur  = self.__dbConnHandle.cursor
		cur.execute("SELECT * FROM salesdb WHERE prdid="+aItemId+" LIMIT COUNTBY 1 ")
		itemrec = cur.fetchone()
		print(itemrec)
		#add itemrec to the list
		#update the qty to that specific record
		

	def generateBill(self):
		#display all the itemrec along with the bill number
		#increment bill number
		#sum all the items in the list and update data in sales db.
		