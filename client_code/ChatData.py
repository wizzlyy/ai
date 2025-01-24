import anvil.server
#import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

chat = []

def updChat(sender,message):
  if sender == "bot":
    chat.append({"bot":message,"user":None})
    
  elif sender == "user":
    chat.append({"bot":None,"user":message})
    #updChat("bot",anvil.server.call('send_request',message))

def getChat():
  global chat
  return chat