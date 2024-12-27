from ._anvil_designer import MenuRowTemplate
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

class MenuRow(MenuRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    

    self.fade_in = animation.Transition(opacity=[0, 1])
    self.fade_out = reversed(self.fade_in)
    
  def imageLeft_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.descriptionLeft.visible = True
    animation.animate(self.descriptionLeft, self.fade_in, 500)
  def imageLeft_mouse_leave(self, x, y, **event_args):
    animation.animate(self.descriptionLeft, self.fade_out, 500)
    time.sleep(0.5)
    self.descriptionLeft.visible = False

  def imageCenter_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.descriptionCenter.visible = True
    animation.animate(self.descriptionCenter, self.fade_in, 500)
  def imageCenter_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    animation.animate(self.descriptionLeft, self.fade_out, 500)
    time.sleep(0.5)
    self.descriptionCenter.visible = False

  def imageRight_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.descriptionRight.visible = True
    animation.animate(self.descriptionRight, self.fade_in, 500)
  def imageRight_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    animation.animate(self.descriptionRight, self.fade_out, 500)
    time.sleep(0.5)
    self.descriptionRight.visible = False

  def imageLeft_mouse_down(self, x, y, button, keys, **event_args):
    from ..ItemPage import ItemPage
    self.FoodRow = app_tables.food.search(name=self.item["nameLeft"])
    self.Title = self.item["nameLeft"]
    self.Image = self.item["imageLeft"]
    for i in self.FoodRow:
      for v in i:
        if "addDesc" in v:
          self.AddDesc = v[1]
        if "prices" in v:
          self.Prices = v[1]
    #self.raise_event('x-ReadyAlert')
    #anvil.open_form('Menu.ItemPage')
    itemform = ItemPage(title=self.Title,
                       image=self.Image,
                       addDesc=self.AddDesc,
                       prices=self.Prices)
    #alert(content=itemform)
    anvil.open_form(itemform)
