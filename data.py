import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
api_output = response.text
x = json.loads(api_output)

question_data = x["results"]

