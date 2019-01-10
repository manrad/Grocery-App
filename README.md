# Grocery-App
Grocery App Demo created with Postgres and Python. Uses JSON files to simulate customer interaction

Pre-Requisites:

Python 3.7
Postgres DB
windows/Linux



Description
design a class hierarchy to represent the transactions in a grocery store.  Essentially, a grocery store can have multiple registers.  Customers come into the store and checkout items using one of the registers.  They checkout different items and a bill gets generated.  Keep track of the items (you can use a few items as example) that leave the store (inventory) and the total sales.  Write a small program that initializes the items in the store, prints out the inventory and performs a few transactions and then at the end of these transactions, prints out the remaining items in the store and then finally prints out the total sales during the day. Other features include the ability to apply a discount at an item level or a class of items. For example, you may need to apply a discount for all chips varieties. You may have to provide discounts to store employees, or senior citizens. Please design a piece of code to do the same. Please ensure that your code clearly illustrates different OOPs concepts such as polymorphism, inheritance, information hiding, object, class, encapsulation.

Precondition: 1. setup postgres database and provide configuration details in vivirit/json/config.json
              2. create tables provided under vivirit/sql/* sql files


Usage:
    python groceryApp.py --src_discount=0.7 --emp_discount=0.3 --gen_discount=0
