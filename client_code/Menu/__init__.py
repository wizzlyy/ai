from ._anvil_designer import MenuTemplate
from anvil import *
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
    self.menu_dict = []
    counter = 0
    for row in app_tables.food.search():
      if counter % 3 == 0:
        row_dict = {"nameLeft":row['name'],"imageLeft":row['image'],"descriptionLeft":row['briefDesc']}
      elif counter % 3 == 1:
        row_dict["nameCenter"] = row['name']
        row_dict["imageCenter"] = row["image"]
        row_dict["descriptionCenter"] = row['briefDesc']
      elif counter % 3 == 2:
        row_dict["nameRight"] = row['name']
        row_dict["imageRight"] = row["image"]
        row_dict["descriptionRight"] = row['briefDesc']
        self.menu_dict.append(row_dict)
      counter += 1
    self.repeating_panel_1.items = self.menu_dict

  def HomePageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Landing')

  def ChatPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Chat')
    
        
      
    
    
