import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
api_output = response.text
x = json.loads(api_output)

question_data = x["results"]


# question_data = [
#     {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
#        "question": "Video streaming website YouTube was purchased in it&#039;s entirety by Facebook for US$1.65 billion in stock.",
#        "correct_answer": "False", "incorrect_answers": ["True"]},
#       {"type": "boolean", "difficulty": "medium", "category": "Sports",
#        "question": "Skateboarding was included in the 2020 Summer Olympics in Tokyo.",
#        "correct_answer": "True", "incorrect_answers": ["False"]},
#       {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Video Games",
#        "question": "In &quot;Mario Kart 64&quot;, Waluigi is a playable character.",
#        "correct_answer": "False", "incorrect_answers": ["True"]},
#       {"type": "boolean", "difficulty": "medium", "category": "History",
#        "question": "Assyrian king Sennacherib&#039;s destruction of Babylon in 689 BCE was viewed as a triumph by other Assyrian citizens.",
#        "correct_answer": "False", "incorrect_answers": ["True"]},
#       {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
#        "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
#        "correct_answer": "False", "incorrect_answers": ["True"]},
#       {"type": "boolean", "difficulty": "medium",
#        "category": "Entertainment: Cartoon &amp; Animations",
#        "question": "Nutcracker Suite was one of the musical pieces featured in Disney&#039;s 1940&#039;s film Fantasia.",
#        "correct_answer": "True", "incorrect_answers": ["False"]},
#       {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#        "question": "Android versions are named in alphabetical order.",
#        "correct_answer": "True", "incorrect_answers": ["False"]},
#       {"type": "boolean", "difficulty": "medium", "category": "Science: Mathematics",
#        "question": "E = MC3", "correct_answer": "False", "incorrect_answers": ["True"]},
#       {"type": "boolean", "difficulty": "easy", "category": "General Knowledge",
#        "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
#        "correct_answer": "True", "incorrect_answers": ["False"]},
#       {"type": "boolean", "difficulty": "medium",
#        "category": "Entertainment: Japanese Anime &amp; Manga",
#        "question": "The anime Attack on Titan was directed by Tetsur\u014d Araki, the same person who directed the anime Highschool of the Dead.",
#        "correct_answer": "True", "incorrect_answers": ["False"]}]
