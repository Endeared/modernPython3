import requests
from random import choice

headers = {
    "accept": "application/json"
}
params = {
    "term": input("Let me tell you a joke! Give me a topic:\n")
}
response = requests.get(
    "https://icanhazdadjoke.com/search",
    headers=headers,
    params=params
)

data = response.json()
results = data["results"]
jokeCount = data["total_jokes"]

if jokeCount > 1:
    print(
        f"I've got {jokeCount} jokes about {params['term']}. Here's one:\n",
        choice(results)['joke']
    )
elif jokeCount == 1:
    print(
        f"I've got one joke about {params['term']}. Here it is:\n",
        results[0]['joke']
    )
else:
    print(f"Sorry, I don't have any jokes about {params['term']}! Please try again.")
