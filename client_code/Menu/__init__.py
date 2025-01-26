from ._anvil_designer import MenuTemplate
from anvil import *
#import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import math

class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.organiseTable(app_tables.menu.search())
    sortList = []
    for row in app_tables.categories.search():
        sortList.append((row["Category"], row))
    
    self.sortDropDown.items = sortList

  # Open Forms
  def HomePageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Landing')
  def ChatPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Chat')
  def OrderButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Order")

  def searchButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    searchReq = self.searchBox.text
    if searchReq:
      searchData = anvil.server.call('searchMenu',searchItem=searchReq)
      self.organiseTable(searchData)
    else:
      searchData = app_tables.menu.search()
      self.organiseTable(searchData)
      
  def organiseTable(self,data):
    self.menu_dict = []
    counter = 0
    for row in data:
      if counter % 3 == 0:
        row_dict = {"nameLeft":row["name"],"imageLeft":row["mainImage"],"addImageLeft":[row["addImage1"],row["addImage2"]],"descriptionLeft":row["briefDesc"]}
        self.menu_dict.append(row_dict)
      elif counter % 3 == 1:
        self.menu_dict[math.floor(counter/3)]["nameCenter"] = row['name']
        self.menu_dict[math.floor(counter/3)]["imageCenter"] = row['mainImage']
        self.menu_dict[math.floor(counter/3)]["addImageCenter"] = [row['addImage1'],row['addImage2']]
        self.menu_dict[math.floor(counter/3)]["descriptionCenter"] = row['briefDesc']
        
      elif counter % 3 == 2:
        self.menu_dict[math.floor(counter/3)]["nameRight"] = row['name']
        self.menu_dict[math.floor(counter/3)]["imageRight"] = row['mainImage']
        self.menu_dict[math.floor(counter/3)]["addImageRight"] = [row['addImage1'],row['addImage2']]
        self.menu_dict[math.floor(counter/3)]["descriptionRight"] = row['briefDesc']
        
        
      counter += 1
      
    self.menuPanel.items = self.menu_dict

  def searchBox_pressed_enter(self, **event_args):
    self.searchMenuTable()
  def sortDropDown_change(self, **event_args):
    self.searchMenuTable()
  def popularityBox_change(self, **event_args):
    self.searchMenuTable()
        
      
  def searchMenuTable(self):
    searchReq = self.searchBox.text
    dropDownReq = self.sortDropDown.selected_value
    popularityReq = self.popularityBox.checked
    searchData = anvil.server.call('searchMenu',searchItem=searchReq,dropDownItem=dropDownReq,popularitySort=popularityReq)
    self.organiseTable(searchData)
    
