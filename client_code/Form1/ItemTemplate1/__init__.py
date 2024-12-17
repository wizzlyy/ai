from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import animation
import time

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    

    self.fade_in = animation.Transition(opacity=[0, 1])
    self.fade_out = reversed(self.fade_in)
    
  def imageLeft_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.descriptionleft.visible = True
    animation.animate(self.descriptionleft, self.fade_in, 500)
  def imageLeft_mouse_leave(self, x, y, **event_args):
    animation.animate(self.descriptionleft, self.fade_out, 500)
    time.sleep(0.5)
    self.descriptionleft.visible = False