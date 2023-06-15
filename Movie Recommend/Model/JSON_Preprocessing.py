import json
import pprint

with open('Model/response.json') as f:
    origin = json.load(f)

print(origin[1]['results'][1]['original_title'])

new_dict = {}

for i in range(len(origin)):
    contents = origin[i]['results']
    for j in range(len(contents)):
        movie_ID = contents[j]['id']
        movie_title = contents[j]['original_title']
        movie_tags = contents[j]['genre_ids']
        new_dict[movie_ID] = [movie_title, movie_tags]

pprint.pprint(new_dict)