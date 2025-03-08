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

    #Changing visiblity
    self.cWarning.visible = False
    self.aWarning.visible = False
    self.sWarning.visible = False
    self.tWarning.visible = False
    self.hWarning.visible = False
    self.mWarning.visible = False

    #Changing statuses
    self.cDone = False
    self.aDone = False
    self.sDone = False
    self.hDone = False
    self.mDone = False
    
  def cBox_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.cBox.text.isdigit():
      self.cDone = False
      self.cWarning.visible = True
      self.cWarning.text = "Input needs to be a number"
    else:
      self.cDone = True
      self.cWarning.visible = False

  def sBox_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.sBox.text.isdigit():
      self.sDone = False
      self.sWarning.visible = True
      self.sWarning.text = "Input needs to be a number"
    else:
      self.sDone = True
      self.sWarning.visible = False

  def aBox_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if not self.aBox.text.isdigit():
      self.aDone = False
      self.aWarning.visible = True
      self.aWarning.text = "Input needs to be a number"
    else:
      self.aDone = True
      self.aWarning.visible = False

  def datePick_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

  def hourTb_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if len(str(self.hourTb.text)) > 2:
      self.hWarning.visible = True
      self.hWarning.text = "Input must be 2 numbers at most"
      self.hDone = False
    elif not self.hourTb.text.isdigit():
      self.hWarning.visible = True
      self.hWarning.text = "Input needs to be a number"
      self.hDone = False
    else:
      if self.timeSelect.selected_value == "AM" and int(self.hourTb.text) != 11:
        self.hWarning.visible = True
        self.hWarning.text = "Time slot is not availible"
        self.hDone = False
      elif self.timeSelect.selected_value == "PM" and ((int(self.hourTb.text) > 9 and int(self.hourTb.text) != 12) or int(self.hourTb.text) <= 0):
        self.hWarning.visible = True
        self.hWarning.text = "Time slot is not availible"
        self.hDone = False
      else:
        self.hWarning.visible = False
        self.hDone = True

  def minTb_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if len(str(self.minTb.text)) > 2:
      self.mWarning.visible = True
      self.mWarning.text = "Input must be 2 numbers at most"
      self.mDone = False
    elif not self.minTb.text.isdigit():
      self.mWarning.visible = True
      self.mWarning.text = "Input needs to be a number"
      self.mDone = False
    else:
      if self.timeSelect.selected_value == "AM" and (int(self.minTb.text) < 30 or int(self.minTb.text) > 59):
        self.mWarning.visible = True
        self.mWarning.text = "Time slot is not availible"
        self.mDone = False
      elif self.timeSelect.selected_value == "PM":
        if not self.hourTb.text.isdigit():
          self.mWarning.visible = True
          self.mWarning.text = "Fill in hour box first."
          self.mDone = False
        elif int(self.hourTb.text) == 9 and (int(self.minTb.text) < 0 or int(self.minTb.text) > 45):
          self.mWarning.visible = True
          self.mWarning.text = "Time slot is not availible"
          self.mDone = False
        elif int(self.minTb.text) < 0 or int(self.minTb.text) > 59:
          self.mWarning.visible = True
          self.mWarning.text = "Time slot is not availible"
          self.mDone = False
        else:
          self.mWarning.visible = False
          self.mDone = True
      else:
        self.mWarning.visible = False
        self.mDone = True

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    if self.aDone and self.sDone and self.cDone and self.hDone and self.mDone:
      

  def payButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.totalLabel.text == "":
      self.tWarning.visible = True
      self.tWarning.text = "All blanks must be filled to calculate the total cost."
    

  

    
    
  