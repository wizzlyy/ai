from ._anvil_designer import MenuTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.organiseTable(app_tables.menu.search())

  def HomePageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Landing')

  def ChatPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Chat')

  def OrderButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Order")

  def MenuPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def searchButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    searchReq = self.searchBox.text
    if not searchReq.isspace() and searchReq != "":
      searchData = anvil.server.call('searchMenu',searchItem=searchReq)
      self.organiseTable(searchData)
      print(searchData)
      
  def organiseTable(self,data):
    self.menu_dict = []
    counter = 0
    for row in data:
      if counter % 3 == 0:
        row_dict = {"nameLeft":row['name'],"imageLeft":row['mainImage'],"descriptionLeft":row['briefDesc'],"addImageLeft":[row['addImage1'],row['addImage2']]}
      elif counter % 3 == 1:
        row_dict["nameCenter"] = row['name']
        row_dict["imageCenter"] = row['mainImage']
        row_dict["addImageCenter"] = [row['addImage1'],row['addImage2']]
        row_dict["descriptionCenter"] = row['briefDesc']
      elif counter % 3 == 2:
        row_dict["nameRight"] = row['name']
        row_dict["imageRight"] = row['mainImage']
        row_dict["addImageRight"] = [row['addImage1'],row['addImage2']]
        row_dict["descriptionRight"] = row['briefDesc']
        self.menu_dict.append(row_dict)
      counter += 1
    self.menuPanel.items = self.menu_dict
        
      
    
    
