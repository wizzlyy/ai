from ._anvil_designer import LandingTemplate
from anvil import *
#import stripe.checkout
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
    # Login
    anvil.users.login_with_form()
    self.currentUser = anvil.server.call('get_user_email')

    #Page Layout
    self.GreetingLabel.text = f"Hello, {self.currentUser['email']}, what would you like to do today?"

  # Open Forms
  def MenuPageButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Menu")
  def OrderButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Order")
  def chatButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Chat")
    