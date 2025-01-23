import anvil.secrets
import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def get_user_email():
  return anvil.users.get_user(allow_remembered=True)

"""@anvil.server.callable
def updateFoodList(food,price,quantity):
  if app_tables.foodorder.get(Food=food) is None:
    app_tables.foodorder.add_row(Food=food,Quantity=quantity,Price=price)
  else:
    app_tables.foodorder.get(Food=food).update(Price=price,Quantity=quantity)

@anvil.server.callable
def deleteFoodList(food):
  app_tables.foodorder.get(Food=food).delete()

@anvil.server.callable
def getFoodOrder():
  return app_tables.foodorder.search()

@anvil.server.callable
def getFoodRow(food):
  return app_tables.foodorder.get(Food=food)"""

@anvil.server.callable
def searchMenu(searchItem):
  return app_tables.menu.search(q.any_of(name=q.ilike(searchItem),
                                         category=q.ilike(searchItem)))
