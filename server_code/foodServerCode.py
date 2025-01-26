import anvil.secrets
#import anvil.stripe
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

@anvil.server.callable
def searchMenu(searchItem,dropDownItem,popularitySort = False):
  if dropDownItem != "None":
    categoryOfTable = []
    for row in app_tables.menu.search():
      categoryMenu = row[4][1]
      if categoryMenu == dropDownItem:
        categoryOfTable.append(row)
    if searchItem != "" and searchItem.isspace() is False:
      qtable = app_tables.menu.search(q.any_of(name=q.ilike(searchItem)))
    else:
      qtable = app_tables.menu.search()
    chosenTable = []
    print(categoryOfTable)
    for row in qtable:
      if row in categoryOfTable:
        chosenTable.append(row)
    print(chosenTable)
  else:
    categoryOfTable = app_tables.menu.search()
    chosenTable = categoryOfTable(q.any_of(name=q.ilike(searchItem),category=q.ilike(searchItem)))
  
  if popularitySort:
    return chosenTable.order_by(ascending=False)
  else:
    return chosenTable
                                
      
