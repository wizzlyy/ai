import anvil.secrets
#import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json
import requests
from . import ChatData

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


@anvil.server.callable
def send_request(user_prompt):
  global URL
  global HEADERS
  prompt = f"""
this is a restaurant chatbot.
you are to tell me what the prompt is asking for. 
take what they ask at face value, and that there is no deeper meaning.
reply with the most suited catergory in the below 3 answers.
if the prompt does not explicitly ask for one of the 3 catergories, then it belongs in (other), you do not have to think of the customer's intentions, just look at the request.
when an input is asked for, do not output the original instructions, such as do not output "food that was asked for from the request this should be replaced by the input", instead output what the instruction asks for.
respond using json.

- menu (asking for menu only), if they ask for a specific food, state it in this manner. If the food is not specificed, foodinput would be null. Please also consider yourself whether the foodinput input is valid, (for example, it is a integer or you cannot understand it) if it is not valid, return null for foodinput, and response asking to clarify.{"{'request_type': 'menu', 'foodinput': input, 'response': your response}"}
- recommendations (asking for recommendations only), state it in this manner {"{'request_type': 'recommendation', 'response': your response}"}
- reservation (asking for reservations only), If the amount of people is not specificed, num_people would be null. Please also consider yourself whether the num_people input is valid, for example, it is a integer, if it is not, return null for num_people. {"{'request_type': reservation, 'num_people': input, 'response': your response}"}
- ordering (asking to order a food only, NOT paying), also state it in this manner. there should be no integers included in foodinput. {"{'request_type': 'order', 'quantity_of_food': input for quantity of food wanted, 'foodinput': input for what food was wanted, 'response': your response}"}
- pay (asking to pay only), state it in this manner {"{'request_type': 'pay', 'response': your response}"}
- other, look through the chat history and see if the request is related to a question. if it is not, state {"{'request_type': 'other', 'response': 'Please clarify.'}"} Here is the chat history: {ChatData.getChat()}

latest prompt: {user_prompt}

you are to decide what the latest request is asking for in the chat history and follow the instructions to state it.
do not come up with a python solution.
do not use any context, just sort.
do not give any reasons.
keep all values returned in lower case please, except for your responses.
also give a little response, assume you know nothing about the restaurant, and thus do not come up with any food names or promise any food items. Example: you can respond with "alright. heres the menu:"
all values given in the json statements are required to be returned, do not leave any out.
"""
  data = {"model": "llama3.2",
          "prompt": prompt,
          "stream": False,
          "options": {
            "temperature": 0
          },
          "format": "json"}  
  response = requests.post(url=URL, headers=HEADERS, data=json.dumps(data))
  response_data = json.loads(response.text)
  return json.loads(response_data["response"])
  