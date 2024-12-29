from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.quantity = 0
    self.price = 0
    # Any code you write here will run before the form opens.
    self.updateRow()
  
  def upQuantity_click(self, **event_args):
    print("click")
    foodPrice = app_tables.menu.get(name=self.item["Food"])['prices']
    anvil.server.call('updateFoodList',food=self.item["Food"],price=str(float(foodPrice)*int(self.quantity+1)),quantity=self.quantity+1)
    self.updateRow()
    self.parent.raise_event("x-updateTotal")
  def downQuantity_click(self, **event_args):
    print("click")
    if self.item["Quantity"] > 0:
      foodPrice = app_tables.menu.get(Food=self.item["Food"])["prices"]
      anvil.server.call('updateFoodList',food=self.item["Food"],price=str(float(foodPrice)*int(self.quantity-1)),quantity=self.quantity-1)
      self.updateRow()
      self.parent.raise_event("x-updateTotal")
  def deleteButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('deleteFoodList',food=self.item["Food"])
    self.parent.raise_event("x-updateTotal")
    self.remove_from_parent()
    
  def updateRow(self):
    foodRow = anvil.server.call('getFoodRow',food=self.item["Food"])
    self.quantity = foodRow['Quantity']
    self.price = foodRow['Price']
    self.quantityLabel.text = self.quantity
    self.priceLabel.text = self.price
    