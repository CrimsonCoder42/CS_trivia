import requests

question_type = {
    'amount': 10,
    'type': "boolean",
    "category": 18,
                 }

response = requests.get('https://opentdb.com/api.php', params=question_type)
response.raise_for_status()
trivia_data = response.json()

question_data = trivia_data["results"]


print(question_data)

