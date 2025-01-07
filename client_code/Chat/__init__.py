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
from .. import ChatData

class Chat(ChatTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def sendBox_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if self.sendBox.text and not self.sendBox.text.isspace():
      #anvil.server.call('addChat',message=self.sendBox.text,sender="User")
      #self.chatPanel.items = anvil.server.call('getChat')
      ChatData.updChat(sender="user",message=self.sendBox.text)
      self.chatPanel.items = ChatData.getChat()
      self.sendBox.text = ""
  def sendButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.sendBox.text and not self.sendBox.text.isspace():
      #anvil.server.call('addChat',message=self.sendBox.text,sender="User")
      #self.chatPanel.items = anvil.server.call('getChat')
      ChatData.updChat(sender="user",message=self.sendBox.text)
      self.chatPanel.items = ChatData.getChat()
      self.sendBox.text = ""
  def HomePageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Landing")

  def MenuPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Menu")

  def OrderButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Menu")
    