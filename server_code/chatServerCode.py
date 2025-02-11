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
"""@anvil.server.callable
def addChat(message,sender):
  if sender == "Bot":
    app_tables.chathistory.add_row(Bot=message)
  elif sender == "User":
    app_tables.chathistory.add_row(User=message)

@anvil.server.callable
def getChat():
  return app_tables.chathistory.search()"""

