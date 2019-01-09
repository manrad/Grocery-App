#!/usr/bin/python
# Generates Test commands based on the installed regions and type of NDS map
# For example : Based the type of map release, such as Country specific, region specific, continent specific, world map
# the test strategy will be decided and the corresponding test inputs will be pulled automatically for testing.

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
import sys
import time
import uuid

cur = ''

# just adds items to db from text.json
parser = argparse.ArgumentParser(prog='db_populate', usage='%(prog)s [options]', prefix_chars='--')
parser.add_argument('--itemID', nargs='+', type=str, help='start time of job execution',required=True)
parser.add_argument('--itemClass', nargs='+', type=str,help=' end time of job execution',required=True)
parser.add_argument('--mrp', nargs='+', type=float, help='mapname to be tested',required=True)
parser.add_argument('--disc', nargs='+', type=float, help='discount',required=True)
args = parser.parse_args()
#print (args.itemID[0])

try:
    conn = psycopg2.connect("dbname='grocery' user='postgres' host='127.0.0.1' port='5433' password='#09RameshIBM'")

except:
    print ("I am unable to connect to the database")
    conn = "NULL"

if(conn != "NULL"):
	cur = conn.cursor()
else:
	print("cannot get cursor")

#check for availability of items.json, to populate the db
with open('items.json') as data_file:    
	jdata = json.load(data_file)
	for jitemclass in jdata:
		for jitem in jdata[jitemclass]:
			#print(jdata[jitemclass][jitem]["mrp"])
			mrp = jdata[jitemclass][jitem]["mrp"]
			qty = jdata[jitemclass][jitem]["qty"]
			disc = jdata[jitemclass][jitem]["disc"]
			cur.execute("INSERT INTO public.itemsdb (itemclass,mrp,prdid,qty,disc) VALUES (%s, %s, %s, %s, %s)", \
						(jitemclass,mrp,jitem,qty,disc))

conn.commit()
cur.close()
conn.close()