import json
import common
import db_handler
import billgen
NULL = 0
TRUE = 1
FALSE = 0
#responsibility
#	1.to store sales data

#collaboration
#	uses dbHandler::getDB static instance to get cursor to DB

class salesHandler:


	# instance attribute
	def __init__(self):
		self.flag = TRUE
		
	def additem(self,aDbHandle, aItemName, aMrp, aDisc, aQty, aSalesPrice, aDateVar, aBillName):
		itemList = None
		if aDbHandle != NULL:
			cur = aDbHandle.cursor()
			#INSERT ITEM SALES							
			cur.execute("INSERT INTO public.salesdb (bill,itemid,qty,salesprice,mrp,disc,billdate) VALUES (%s, %s ,%s, %s, %s, %s, %s)",\
				(aBillName,aItemName,aQty,aSalesPrice,aMrp,aDisc,aDateVar))
			aDbHandle.commit()
			cur.close()
			itemList = 1
		else:
			print("error creating entries in DB")
		return itemList
			
	def addBillInfo(self,aDbHandle,aTotalPrice, aDateVar, aBillName):
		itemList = None
		if aDbHandle != NULL:
			cur = aDbHandle.cursor()
			#INSERT ITEM SALES							
			cur.execute("INSERT INTO public.billsales (billno,dateinfo,totalsales) VALUES (%s, %s ,%s)",\
				(aBillName,aDateVar,aTotalPrice))
			aDbHandle.commit()
			cur.close()
			itemList = 1
		else:
			print("error creating entries in DB")
		return itemList
