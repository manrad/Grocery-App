#!/usr/bin/python
from customer import srCitizen
from customer import employeeCustomer
class fac_customer(object):
	def __init__(self,disc_srCitizen,disc_emp,disc_gen):
		self.__srCitizenDiscount = disc_srCitizen
		self.__empDiscount = disc_emp
		self.__generalDiscount = disc_gen
		
	def getDiscount(self,custObj):
		if isinstance(custObj,srCitizen):
			return self.__srCitizenDiscount
		elif isinstance(custObj,employeeCustomer):
			return self.__empDiscount
		else:
			return 0