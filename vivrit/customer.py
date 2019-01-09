#!/usr/bin/python

# store employee id range 1500 to 2000

			

class customer:
	# instance attribute
	def __init__(self,age,id):
		self.__age = age
		self.__id = id
		
	def getAge(self):
		return self.__age

	def getId(self):
		return self.__id
		
		
		
class srCitizen(customer):

	def __init(self,age,id):
		base_customer.__init__(age,id)
		
	def isSeniorCitizen(self):
		return TRUE
		
class employeeCustomer(customer):
	def __init(self,age,id):
		base_customer.__init__(age,id)
		
	def isEmployee(self):
		return TRUE

		