import requests
import json

# The base URL for the JokeAPI
base_url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=sexist,explicit"

# base_url = "http://programming-jokes-api.herokuapp.com/jokes/random"

# base_url = "https://official-joke-api.appspot.com/jokes/programming/random"

# Send a GET request to the API
response = requests.get(base_url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to get joke: {response.status_code}")
    exit()



# data = response.json()[0]  # The response is a list, so we take the first element

# print(f"{data['setup']}\n{data['punchline']}")

# Parse the response as JSON
data = response.json()

# Depending on the type of joke (single or two-part), we print it differently
if data['type'] == 'single':
    print(data['joke'])
else:
    print(f"{data['setup']}\n{data['delivery']}")
