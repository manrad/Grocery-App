#!/usr/bin/python
import json
import psycopg2
from psycopg2 import extras
NULL = 0
#responsibility
#	1.read data from config.json
#	2.establish connection with database
#	3.return db handle

#collaboration
#	uses dbHandler::getDB static instance to get cursor to DB
class db_handler:

	def __init__(self):
		self.__db_Instance = NULL
		
	def getDBConnHandle(self):
		if self.__db_Instance == NULL:
			with open('./json/config.json') as data_file:    
				jdata = json.load(data_file)
				cdbname = jdata["dbname"]
				cdbuser = jdata["dbuser"]
				cdbhost = jdata["dbhost"]
				cdbport = jdata["dbport"]
				cdbpwd = jdata["dbpwd"]
				try:
					cfgstr = "dbname="+cdbname+" user= "+cdbuser+"  host="+cdbhost+" port = "+cdbport+" password="+cdbpwd+""
					#print(cfgstr)
					self.__db_Instance = psycopg2.connect(cfgstr)
				except:
					print("unable to connect to db %s",cdbname + cdbuser + cdbhost +cdbport +cdbpwd)
					self.__db_Instance = NULL
		return self.__db_Instance
		
