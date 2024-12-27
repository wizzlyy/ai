from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()
    self.currentUser = anvil.server.call('get_user_email')
    
    self.GreetingLabel.text = f"Hello, {self.currentUser['email']}, what would you like to do today?"

  def MenuPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Menu")
    