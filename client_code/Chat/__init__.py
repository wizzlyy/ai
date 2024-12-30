from ._anvil_designer import ChatTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Chat(ChatTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def sendBox_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if self.sendBox.text:
      anvil.server.call('addChat',message=self.sendBox.text,sender="User")
      self.chatPanel.items = anvil.server.call('getChat')

  def sendButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.sendBox.text:
      anvil.server.call('addChat',message=self.sendBox.text,sender="User")
      self.chatPanel.items = anvil.server.call('getChat')
    