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

# Updates the Chat
def updChat(sender,message):
  global chat
  if sender == "bot":
    chat.append({"role":"assistant","content":message})
  elif sender == "user":
    chat.append({"role":"user","content":message})
    response = anvil.server.call('send_request',message,chat)
    updChat("bot",response)

# Returns the Chat
def getChat():
  global chat
  return chat