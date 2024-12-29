from ._anvil_designer import ItemPageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import animation
import time

class ItemPage(ItemPageTemplate):
  def __init__(self, title, image, addDesc, prices, addImage, **properties):
    # Set Form properties and Data Bindings.
    self.title = title
    self.image = image
    self.addDesc = addDesc
    self.prices = prices
    self.addImage = addImage
    self.quantity = 1
    self.counter = 0
    
    self.addImage.insert(0,self.image)
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.fade_in = animation.Transition(opacity=[0, 1])
    self.fade_out = reversed(self.fade_in)
    
    self.imageBox.source = self.addImage[self.counter%3]
    self.counter += 1

    self.updateLabels()
    
    
  def imageTimer_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    animation.animate(self.imageBox, self.fade_out, 500)
    time.sleep(0.5)
    self.imageBox.visible = False
    self.imageBox.source = self.addImage[self.counter%3]
    self.counter += 1
    time.sleep(0.1)
    self.imageBox.visible = True
    animation.animate(self.imageBox,self.fade_in, 500)
    time.sleep(0.5)

  def quantityUp_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.quantity += 1
    self.updateLabels()

  def updateLabels(self):
    self.quantityLabel.text = f"x {self.quantity}"
    self.pricesBox.text = f"Price: {self.quantity * float(self.prices)}"

  def quantityDown_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.quantity > 0:
      self.quantity -= 1
      self.updateLabels()

  def backButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert",value="0")

  def addButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert",value=self.pricesBox.text)
