import json
import common
import db_handler
import billgen
NULL = 0
TRUE = 1
FALSE = 0
#responsibility
#	1.initializing items
#	2.set discounts per class/item
#	3.update item

#collaboration
#	uses dbHandler::getDB static instance to get cursor to DB

class item_manager:


	# instance attribute
	def __init__(self):
		self.flag = TRUE
		
	def initializeItems(self,aDbHandle):
		itemList = NULL
		if aDbHandle != NULL:
			cur = aDbHandle.cursor()
			cur.execute("DELETE FROM public.itemsdb")
			cur.execute("DELETE FROM public.salesdb")
			cur.execute("DELETE FROM public.billsales")
			with open('./json/items.json') as data_file:    
				jdata = json.load(data_file)
				for jitemclass in jdata:
					for jitem in jdata[jitemclass]:
						#print(jdata[jitemclass][jitem]["mrp"])
						mrp = jdata[jitemclass][jitem]["mrp"]
						qty = jdata[jitemclass][jitem]["qty"]
						cur.execute("INSERT INTO public.itemsdb (itemclass,mrp,prdid,qty) VALUES (%s, %s, %s, %s)", \
									(jitemclass,mrp,jitem,qty))
			aDbHandle.commit()
			cur.close()
		else:
			print("error creating entries in DB")
		return itemList
			

	#setDiscount
	#ability to set discount/class/item
	# aType is EClass, EItem
	# aName is EClassName, EClassItem
	# aDiscount in number of percentage double: 10.5% is 10.5
	# return retStatus : NULL on Failure, 1 on success
	def setDiscount(self,aDbHandle, aType,aName,aDiscount):
		retStatus = NULL
		if aDbHandle != NULL:
			cur = aDbHandle.cursor()
			if aType == common.itemType.EItemClass:
				updQry = """UPDATE public.itemsdb SET disc = %s WHERE itemclass = %s"""
				cur.execute(updQry, (aDiscount,aName))
				#cur.execute("SELECT * FROM itemsdb")
				retStatus = 1
			if aType == common.itemType.EItem:
				updQry = """UPDATE public.itemsdb SET disc = %s WHERE prdid = %s"""
				cur.execute(updQry, (aDiscount,aName))			
				#cur.execute("UPDATE public.itemsdb SET disc = (%s) WHERE prdid = (%s)", (aDiscount,aName))
				retStatus = 1
			aDbHandle.commit()
			cur.close()
		else:
			print("Handle not available: Ensure InitializeItems is called before invoking setDiscount")
		return retStatus

	# getBatchItems
	# getCompleteRecord for all the items in the object
	# aObj : list containing all the checkout items
	# aResObj : list containing complete record for all checkedout items
	def getBatchItems(self,aDbHandle,aObj):
		resObj = NULL
		prdstr = "prdid"
		qStr = ""
		stat = NULL
		for obj in aObj:
			if stat == NULL:
				qStr = qStr + " prdid = \'" + obj + "\'"
				stat = 1
			else:
				qStr = qStr + " OR prdid = \'" + obj + "\'"
				
		if aDbHandle != NULL:
			cur = aDbHandle.cursor()
			selQuery = "SELECT * FROM public.itemsdb WHERE " + qStr
			cur.execute(selQuery)
			resObj = cur.fetchall()
			#print (resObj)
			cur.close()
		return resObj

	# getItemData
	# getCompleteRecord for all specific item
	# aPrdId : item for which the data to be fetched 
	# aResObj : list containing complete record for all checkedout items
	def getItemData(self,aDbHandle,aPrdId):
		resObj = NULL
		qStr = ""
		stat = NULL
		qStr = qStr + " prdid = \'" + aPrdId + "\'"
		if aDbHandle != NULL:
			cur = aDbHandle.cursor()
			selQuery = "SELECT * FROM public.itemsdb WHERE " + qStr
			cur.execute(selQuery)
			resObj = cur.fetchone()
			#print (resObj)
			cur.close()
		return resObj		
		
	#updateItemQty
	#ability to updateItem Qty for a specific item
	# aItemName Item name
	# aQty Number of Quantity
	#return None else billgen obj
	def updateItemQty(self,aDbHandle,aItemName,aQty,special_disc):
		billgenobj = None
		if self.flag == TRUE :
			self.flag = FALSE
			if aDbHandle != NULL :
				cur = aDbHandle.cursor()
				# get Element first
				selQry = "SELECT * FROM public.itemsdb WHERE prdid = \'" + aItemName + "\'"
				cur.execute(selQry)
				itemrec = cur.fetchone()
				totsastr = "%5.2f"% itemrec[4]
				#print(str(itemrec[0]) +"    	" + str(itemrec[1]) +"    	    	" + str(itemrec[5]) + "   	   	" +totsastr)
				#print("itemrec %s",itemrec)
				# TBD Change qty value and update in DB
				qty = itemrec[1]
				qty = qty - aQty
				updQry = """UPDATE public.itemsdb SET qty = %s WHERE prdid = %s"""
				cur.execute(updQry, (qty,aItemName))
				aDbHandle.commit()
				mrp = itemrec[4]
				disc = itemrec[5]
				if disc == None:
					disc = 0
				if special_disc == None:
					special_disc = 0
				total_disc = disc #should not have special discounts
				disc_price = mrp  - mrp * (total_disc)/100
				#return bill gen Object
				billgenobj = billgen.billGen(itemrec[2],itemrec[4],aQty,total_disc,disc_price)
				self.flag = TRUE
				cur.close()
			return billgenobj

	#update
	def updateSalesDB(self,aDbHandle,aItemName,aQty,special_disc):
		billgenobj = None
		if self.flag == TRUE :
			self.flag = FALSE
			if aDbHandle != NULL:
				cur = aDbHandle.cursor()
				# get Element first
				selQry = "SELECT * FROM public.itemsdb WHERE prdid = \'" + aItemName + "\'"
				cur.execute(selQry)
				itemrec = cur.fetchone()
				print("itemrec %s",itemrec)
				# TBD Change qty value and update in DB
				qty = itemrec[1]
				qty = qty - aQty
				updQry = """UPDATE public.itemsdb SET qty = %s WHERE prdid = %s"""
				cur.execute(updQry, (qty,aItemName))
				self.__dbConnHandle.commit()
				mrp = itemrec[4]
				disc = itemrec[5]
				if disc == None:
					disc = 0
				if special_disc == None:
					special_disc = 0
				total_disc = special_disc + disc
				disc_price = mrp  - mrp * (total_disc)/100
				#return bill gen Object
				billgenobj = billgen.billGen(itemrec[2],itemrec[1],aQty,total_disc,disc_price)
				self.flag = TRUE
				cur.close()
			return billgenobj			