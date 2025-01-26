from ._anvil_designer import OrderRowTemplate
from anvil import *
#import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import OrderData

class OrderRow(OrderRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.quantity = 0
    self.price = 0
    # Any code you write here will run before the form opens.
    self.updateRow()
  
  def upQuantity_click(self, **event_args):
    #foodPrice = app_tables.menu.get(name=self.item["Food"])['prices']
    #anvil.server.call('updateFoodList',food=self.item["Food"],price=str(float(foodPrice)*int(self.quantity+1)),quantity=self.quantity+1)
    #self.updateRow()
    foodPrice = app_tables.menu.get(name=self.item["food"])["prices"]
    OrderData.updRow(food=self.item["food"],price=str(float(foodPrice)*int(self.quantity+1)),quantity=self.quantity+1)
    self.updateRow()
    self.parent.raise_event("x-updateTotal")
    
  def downQuantity_click(self, **event_args):
    if self.item["quantity"] > 0:
      foodPrice = app_tables.menu.get(name=self.item["food"])["prices"]
      #anvil.server.call('updateFoodList',food=self.item["Food"],price=str(float(foodPrice)*int(self.quantity-1)),quantity=self.quantity-1)
      OrderData.updRow(food=self.item["food"],price=str(float(foodPrice)*int(self.quantity-1)),quantity=self.quantity-1)
      self.updateRow()
      self.parent.raise_event("x-updateTotal")
      
  def deleteButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    #anvil.server.call('deleteFoodList',food=self.item["Food"])
    OrderData.delRow(self.item["food"])
    self.parent.raise_event("x-updateTotal")
    self.remove_from_parent()
    
  def updateRow(self):
    #foodRow = anvil.server.call('getFoodRow',food=self.item["Food"])
    #self.quantity = foodRow['Quantity']
    #self.price = foodRow['Price']
    foodRow = OrderData.getRow(self.item["food"])
    self.quantity = foodRow["quantity"]
    self.price = foodRow["price"]
    self.quantityLabel.text = foodRow["quantity"]
    self.priceLabel.text = foodRow["price"]
    