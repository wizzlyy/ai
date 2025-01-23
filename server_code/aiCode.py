import anvil.secrets
import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
import anvil.secrets

URL = anvil.secrets.get_secret("url")
HEADERS = {"Content-Type": "application/json"}

global url

@anvil.server.callable
def send_request(prompt):
  data = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False
  }
  response = requests.post(url=url, headers=headers, data=json.dumps(data))
  response_data = json.loads(response.text)
  return response_data["response"]
  