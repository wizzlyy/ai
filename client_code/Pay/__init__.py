from ._anvil_designer import PayTemplate
from anvil import *
import anvil.server
import stripe
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Pay(PayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    stripe.api_key = anvil.server.call('getKey')
    # Any code you write here will run before the form opens.
    self.totalLabel.text = "All blanks need to be filled in!"

  def cBox_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.cBox.text.isdigit():
      self.cWarning.visible = True
      self.cWarning.text = "Input needs to be a number"
    else:
      self.cWarning.visible = False

  def sBox_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.sBox.text.isdigit():
      self.sWarning.visible = True
      self.sWarning.text = "Input needs to be a number"
    else:
      self.sWarning.visible = False

  def aBox_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.aBox.text.isdigit():
      self.aWarning.visible = True
      self.aWarning.text = "Input needs to be a number"
    else:
      self.aWarning.visible = False

  def datePick_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

  def hourTb_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.hourTb.text.isdigit():
      self.hWarning.visible = True
      self.hWarning.text = "Input needs to be a number"
    else:
      if self.timeSelect.selected_value == "AM" and int(self.hourTb.text) != 11:
        self.hWarning.visible = True
        self.hWarning.text = "Time slot is not availible"
      elif self.timeSelect.selected_value == "PM" and ((int(self.hourTb.text) > 9 and int(self.hourTb.text) != 12) or int(self.hourTb.text) <= 0):
        self.hWarning.visible = True
        self.hWarning.text = "Time slot is not availible"
      else:
        self.hWarning.visible = False

  def minTb_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.minTb.text.isdigit():
      self.mWarning.visible = True
      self.mWarning.text = "Input needs to be a number"
    else:
      if self.timeSelect.selected_value == "AM" and (int(self.minTb.text) < 30 or int(self.minTb.text) > 59):
        self.mWarning.visible = True
        self.mWarning.text = "Time slot is not availible"
      elif self.timeSelect.selected_value == "PM":
        if not self.hourTb.text.isdigit():
          self.mWarning.visible = True
          self.mWarning.text = "Fill in hour box first."
        elif int(self.hourTb.text) == 9 and (int(self.minTb.text) < 0 or int(self.minTb.text) > 45):
          self.mWarning.visible = True
          self.mWarning.text = "Time slot is not availible"
        elif int(self.minTb.text) < 0 or int(self.minTb.text) > 59:
          self.mWarning.visible = True
          self.mWarning.text = "Time slot is not availible"
        else:
          self.mWarning.visible = False
      else:
        self.mWarning.visible = False

  

    
    
  