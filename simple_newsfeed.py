''' 
Created by Ryan Bautista on 12/29/16.
simple_newsfeed.py is powered by NewsAPI: https://newsapi.org
All rights reserved

'''

import requests
import json
import random
from sources import sources_dict

your_api_key = '5f8c9be7dc664fa4a3ee8311ce5322b6'

random_source = random.sample(sources_dict.keys(), 3)

print("Find and read today's top headlines from 70 sources!")

print("For example, you can choose from", end=' ')

for i in range(len(random_source)):
    print(random_source[i], end=', ')

print("etc.")

user_input = input('What news source would you like to see? Type "help" to see full list. \n')

while True:
    if(user_input == "help"):
        for keys in sources_dict.keys():
            print(keys)
        user_input = input('What news source would you like to see? ')
        continue
    else:
        try:
            source_query = sources_dict[user_input]
            break
        except KeyError:
            user_input = input('That is not a valid news source. Enter again: ')
            continue

url = 'https://newsapi.org/v1/articles?source=' + source_query + '&sortBy=top&apiKey=' + your_api_key

r = requests.get(url)

parsed_json = json.loads(r.text)  # turn JSON text into readable dictionary 

for i in range(0, len(parsed_json['articles'])):
    print()
    headline = parsed_json['articles'][i]['title']
    print(str(i + 1) + ") \"" + headline + "\"")
    print("   Link:", parsed_json['articles'][i]['url'])

print("\nPowered by NewsAPI: https://newsapi.org")
