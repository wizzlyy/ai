from ._anvil_designer import MenuRowTemplate
from anvil import *
#import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import animation
import time
from ... import OrderData

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
    self.FoodDetails = app_tables.menu.search(name=self.item["nameLeft"])
    self.Title = self.item["nameLeft"]
    self.Image = self.item["imageLeft"]
    self.AddImage = self.item["addImageLeft"]
    
    for i in self.FoodDetails:
      for v in i:
        if "addDesc" in v:
          self.AddDesc = v[1]
        if "prices" in v:
          self.Prices = v[1]
    self.callOrderForm()

  def imageCenter_mouse_down(self, x, y, button, keys, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    self.FoodDetails = app_tables.menu.search(name=self.item["nameCenter"])
    self.Title = self.item["nameCenter"]
    self.Image = self.item["imageCenter"]
    self.AddImage = self.item["addImageCenter"]
    
    for i in self.FoodDetails:
      for v in i:
        if "addDesc" in v:
          self.AddDesc = v[1]
        if "prices" in v:
          self.Prices = v[1]
    self.callOrderForm()

  def imageRight_mouse_down(self, x, y, button, keys, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    self.FoodDetails = app_tables.menu.search(name=self.item["nameRight"])
    self.Title = self.item["nameRight"]
    self.Image = self.item["imageRight"]
    self.AddImage = self.item["addImageRight"]
    
    for i in self.FoodDetails:
      for v in i:
        if "addDesc" in v:
          self.AddDesc = v[1]
        if "prices" in v:
          self.Prices = v[1]
    self.callOrderForm()





    
  def callOrderForm(self):
    from ..FoodInfoPage import FoodInfoPage
    foodForm = FoodInfoPage(title=self.Title,
                       image=self.Image,
                       addDesc=self.AddDesc,
                       prices=self.Prices,
                       addImage = self.AddImage)
    answer = alert(
      content=foodForm,
      title="Food Info",
      large=True,
      dismissible=False
    )
    if answer is not None:
      foodAns = answer[0]
      quantityAns = answer[1]
      priceAns = str(float(answer[2])*int(quantityAns))
      #anvil.server.call('updateFoodList',food=foodAns,price=priceAns,quantity=quantityAns)

      e = False
      v = OrderData.getOrder()
      for i in v:
        if i["food"] == foodAns:
          e = True
          i["quantity"] += quantityAns
          i["price"] += priceAns
          
      if e is False:
        v.append({"food":foodAns,"quantity":quantityAns,"price":priceAns})
      OrderData.updOrder(v)
        


