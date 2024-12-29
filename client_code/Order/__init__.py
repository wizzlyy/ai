from ._anvil_designer import OrderTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Order(OrderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.set_event_handler('x-updateTotal', self.updateTotalPrice)
    
    # Any code you write here will run before the form opens.
    self.updateTotalPrice()

  def HomePageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Landing")

  def ChatPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Chat")

  def MenuPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Menu")

  def updateTotalPrice(self, **event_args):
    self.totalPrice = 0
    foodOrder = anvil.server.call('getFoodOrder')
    self.repeating_panel_1.items = foodOrder
    for i in foodOrder:
      self.totalPrice += float(i["Price"])

    self.totalLabel.text = self.totalPrice