import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1
#
#    Module1.say_hello()
#


payAmount = 0
def calculate(a,a_amt,c,c_amt,s,s_amt):
  payAmount = int(a)*a_amt,int(c)*c_amt,int(s)*s_amt
  
  
  
