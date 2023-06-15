import json
import pprint

with open('Model/response.json') as f:
    origin = json.load(f)

print(origin[1]['results'][1]['original_title'])

res = {}

for i in range(len(origin)):
    contents = origin[i]['results']
    for j in range(len(contents)):
        new_dict = {}
        new_dict['ID'] = contents[j]['id']
        new_dict['Title'] = contents[j]['original_title']
        new_dict['Tags'] = contents[j]['genre_ids']
        res[contents[j]['id']] = new_dict
output = json.dumps(res)

pprint.pprint(output)

file_path = 'Model/Result.json'
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(output, file)