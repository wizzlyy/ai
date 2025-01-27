from ._anvil_designer import ChatLineTemplate
from anvil import *
import anvil.server
#import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ChatLine(ChatLineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if self.item["role"] == "assistant":
      self.botLabel.text = f"{self.item['content']}"
      self.botLinear.background = "lightgreen"
      self.botLabel.foreground = "white"
    if self.item["role"] == "user":
      self.userLabel.text = self.item["content"]
      self.userLinear.background = "lightblue"
      self.userLabel.foreground = "white"