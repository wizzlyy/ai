from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
#import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if self.botLabel.text:
      self.botLabel.background = "lightgreen"
    if self.userLabel.text:
      self.userLabel.background = "lightblue"