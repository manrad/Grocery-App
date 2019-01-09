#!/usr/bin/python
import db_handler
import datetime
# gets the data from the db and displays the inventory
class inventory:
	def __init__(self):
		self.initialize = None
		
	def printEntriesInDB(self,aDbHandle):
		if aDbHandle != None:
			cur = aDbHandle.cursor()
			print("_____________________________________Inventory List______________________________________________")
			print("id    	    	qty    	    	dsc    	    unitprice")			
			cur.execute("SELECT * FROM public.itemsdb")
			objs = cur.fetchall()
			for x in objs:
				totsastr = "%5.2f"% x[4]
				print(str(x[2]) +"    	" + str(x[1]) +"    	    	" + str(x[5]) + "   	   	" +totsastr)
			cur.close()
			return objs
		else:
			return None

	def printItemsSold(self,aDbHandle):
		if aDbHandle != None:
			cur = aDbHandle.cursor()
			print("_____________________________________Items Sold List______________________________________________")
			print("id    	    	qty    	    	dsc    	    saleprice")			
			cur.execute("SELECT * FROM public.salesdb")
			objs = cur.fetchall()
			for x in objs:
				totsastr = "%5.2f"% x[4]
				print(str(x[1]) +"    	" + str(x[2]) +"    	    	" + str(x[5]) + "   	   	" +totsastr)
			cur.close()
			return objs
		else:
			return None
			
	def getTodaySalesList(self,aDbHandle):
		if aDbHandle != None:
			cur = aDbHandle.cursor()
			datevar = datetime.datetime.now()
			print("_____________________________________Total Sales "+ str(datevar) +"_____________________________________")
			print("billno    	    	    	    	 		sales")
			dbQry = "SELECT * FROM public.billsales WHERE dateinfo =" + "\'" + str(datevar) + "\'" 
			cur.execute(dbQry)
			objs = cur.fetchall()
			daysales = 0
			for x in objs:
				#print(x)
				daysales = daysales + x[3]
				totsastr = "%5.2f"% x[3]
				print (x[0]+"    	    	"+totsastr)
			totsato = "%5.2f"% daysales
			print("\n\n  Total Sales Today = " + totsato)
			cur.close()
			return objs
		else:
			return None