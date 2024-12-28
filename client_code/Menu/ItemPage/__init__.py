from ._anvil_designer import ItemPageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
class ItemPage(ItemPageTemplate):
  def __init__(self, title, image, addDesc, prices, **properties):
    # Set Form properties and Data Bindings.
    self.title = title
    self.image = image
    self.addDesc = addDesc
    self.prices = prices
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    #self.set_event_handler('x-ReadyAlert',self.UpdatePage)
    
  #def UpdatePage(self):
    