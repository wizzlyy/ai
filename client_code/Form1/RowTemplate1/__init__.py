from ._anvil_designer import RowTemplate1Template
from anvil import *
from anvil_extras.animation import Transition, animate

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.slide_in_down = Transition(translateY=["-100%", 0])
    
  def imageLeft_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    t = self.slide_in_down | Transition.height_in(self.descriptionLeft)
    animate(self.descriptionLeft, t, duration=900, direction="normal")
