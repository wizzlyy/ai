import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .Order import Module1
#
#    Module1.say_hello()
#

order = {}

def updOrder(dict):
  global order
  order = dict

def getOrder():
  global order
  return order

def getTotalPrice():
  global order
  price = 0
  for i in order:
    price = price + float(i["price"])
  return price

def getRow(food):
  global order
  for i in order:
    if i["food"] == food:
      return i

def delRow(food):
  global order
  for i in order:
    if i["food"] == food:
      del i

def updRow(food,quantity,price):
  global order
  for i in order:
    if i["food"] == food:
      i["quantity"] = quantity
      i["price"] = price