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
    stripe.api_key = anvil.secrets.get_secret("stripe_key")
    # Any code you write here will run before the form opens.

  