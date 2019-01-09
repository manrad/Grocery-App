#!/usr/bin/python
import argparse
import datetime
import json
from pprint import pprint
from pathlib import Path
from pathlib import PurePath
import psycopg2
from psycopg2 import extras
import random
import re
from string import Template
import subprocess

import datetime
import facade_customer
import customer
import db_handler
import inventory
import common
from item_handler import item_manager
from sales_handler import salesHandler

parser = argparse.ArgumentParser(prog='groceryApp', usage='%(prog)s [options]', prefix_chars='--')
parser.add_argument('--src_discount', nargs='+', type=float, help= 'discount for senior citizen',required=True)
parser.add_argument('--emp_discount', nargs='+', type=float,help= 'discount for store employees',required=True)
parser.add_argument('--gen_discount', nargs='+', type=float,help= 'discount for general customers',required=True)
args = parser.parse_args()


registerX = facade_customer.fac_customer(args.src_discount[0],args.emp_discount[0],args.gen_discount[0])
itemMgr =  item_manager()
stock = inventory.inventory()
salesMgr = salesHandler()

specialdiscount = 0
billobjarr = []
#get db connector handle
db_conn = db_handler.db_handler().getDBConnHandle()
if db_conn != None:
		itemMgr.initializeItems(db_conn)
		
		#set discount for class and item from discount_sheet.json
		with open('./json/discount_sheet.json') as data_file:    
			jdata = json.load(data_file)
			for jclass in jdata["class"]:
				classdisc = jdata["class"][jclass]["disc"]
				itemMgr.setDiscount(db_conn, common.itemType.EItemClass, jclass, classdisc)
				
			for jitem in jdata["item"]:
				itemdisc = jdata["item"][jitem]["disc"]
				itemMgr.setDiscount(db_conn, common.itemType.EItem, jitem, itemdisc)
				
		#print inventory
		stock.printEntriesInDB(db_conn)
		
		#customerA:  regular customer at registryA
		custObj = customer.customer(30,0)
		specialdiscount = registerX.getDiscount(custObj)
		totalsales = 0
		datevar = datetime.datetime.now()
		billName = "Register A " + str(datevar)
		with open('./json/simulate_cart.json') as data_file:    
			jdata = json.load(data_file)
			for jobj in jdata["CustomerA"]:
				qty = jdata["CustomerA"][jobj]
				respObj = itemMgr.getItemData(db_conn,jobj)
				#print(respObj)
				billobj = itemMgr.updateItemQty(db_conn,jobj,qty,specialdiscount)
				billobjarr.append(billobj)
		billprice = 0
		totalbillprice = 0
		print("\n\n_________________________________BILL _____________________________________")
		print("____________________"+ billName +" _________________")
		print("itemname" + "	" + "qty" + "		" + "mrp" +  "		" + "disc" + " 		" + "price")
		for obj in billobjarr:
				#display bill
				# update salesdb
				# TBD multiple qty with total price and put in the right corner
				# add total bill and add it to sales.
				strmrp = "%5.2f"% obj.mrp
				billprice = (obj.total_price * obj.qty)
				totprice = "%5.2f"% billprice
				totalbillprice = totalbillprice + billprice
				print(obj.itemname + " 		" +str(obj.qty) +" 		" + strmrp +" 		" + str(obj.disc) +" 		" + totprice)
		totalbillprice = totalbillprice - (totalbillprice * specialdiscount/100) 
		strtotprice = "%5.2f"% totalbillprice
		print(" \n Regular Discount = "+ str(specialdiscount)+ " 	Total Bill Price = "+strtotprice)
		salesMgr.addBillInfo(db_conn,strtotprice,str(datevar),billName)
		
		billobjarr = []
		#customerB:  senior Citizen customer at registryB
		custObj = customer.srCitizen(61,0)
		specialdiscount = registerX.getDiscount(custObj)
		totalsales = 0
		datevar = datetime.datetime.now()
		billName = "Register B " + str(datevar)
		with open('./json/simulate_cart.json') as data_file:    
			jdata = json.load(data_file)
			for jobj in jdata["CustomerB"]:
				qty = jdata["CustomerB"][jobj]
				respObj = itemMgr.getItemData(db_conn,jobj)
				#print(respObj)
				billobj = itemMgr.updateItemQty(db_conn,jobj,qty,specialdiscount)
				billobjarr.append(billobj)
		billprice = 0
		totalbillprice = 0
		print("\n\n_________________________________BILL _____________________________________")
		print("____________________"+ billName +" _________________")
		print("itemname" + "	" + "qty" + "		" + "mrp" +  "		" + "disc" + " 		" + "price")
		for obj in billobjarr:
				#display bill
				# update salesdb
				# TBD multiple qty with total price and put in the right corner
				# add total bill and add it to sales.
				strmrp = "%5.2f"% obj.mrp
				billprice = (obj.total_price * obj.qty)
				totprice = "%5.2f"% billprice
				totalbillprice = totalbillprice + billprice
				print(obj.itemname + " 		" +str(obj.qty) +" 		" + strmrp +" 		" + str(obj.disc) +" 		" + totprice)
		totalbillprice = totalbillprice - (totalbillprice * specialdiscount/100) 
		strtotprice = "%5.2f"% totalbillprice
		print(" \n Regular Discount = "+ str(specialdiscount)+ " 	Total Bill Price = "+strtotprice)
		salesMgr.addBillInfo(db_conn,strtotprice,str(datevar),billName)

		billobjarr = []
		#customerc:  employee customer at registryC
		custObj = customer.employeeCustomer(21,15000)
		specialdiscount = registerX.getDiscount(custObj)
		totalsales = 0
		datevar = datetime.datetime.now()
		billName = "Register C " + str(datevar)
		with open('./json/simulate_cart.json') as data_file:    
			jdata = json.load(data_file)
			for jobj in jdata["CustomerC"]:
				qty = jdata["CustomerC"][jobj]
				respObj = itemMgr.getItemData(db_conn,jobj)
				#print(respObj)
				billobj = itemMgr.updateItemQty(db_conn,jobj,qty,specialdiscount)
				billobjarr.append(billobj)
		billprice = 0
		totalbillprice = 0
		print("\n\n_________________________________BILL _____________________________________")
		print("____________________"+ billName +" _________________")
		print("itemname" + "	" + "qty" + "		" + "mrp" +  "		" + "disc" + " 		" + "price")
		for obj in billobjarr:
				#display bill
				# update salesdb
				# TBD multiple qty with total price and put in the right corner
				# add total bill and add it to sales.
				strmrp = "%5.2f"% obj.mrp
				billprice = (obj.total_price * obj.qty)
				totprice = "%5.2f"% billprice
				totalbillprice = totalbillprice + billprice
				print(obj.itemname + " 		" +str(obj.qty) +" 		" + strmrp +" 		" + str(obj.disc) +" 		" + totprice)
		totalbillprice = totalbillprice - (totalbillprice * specialdiscount/100) 
		strtotprice = "%5.2f"% totalbillprice
		print(" \n Regular Discount = "+ str(specialdiscount)+ " 	Total Bill Price = "+strtotprice)
		salesMgr.addBillInfo(db_conn,strtotprice,str(datevar),billName)
		
		#get the inventory
		stock.printEntriesInDB(db_conn)
		#get the stock list
		stock.getTodaySalesList(db_conn)