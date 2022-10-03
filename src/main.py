import requests
import json

route = "https://api.modrinth.com/v2/"
search_query = "sodium"
r = requests.get(f'{route}search?query={search_query}')
a = json.loads(r.text)
version = "1.16.5"
for hit in a["hits"]:
    print(hit["slug"])
#    print(hit["versions"])
    if version in hit["versions"]:
        print("true\n")
    else:
        print("false\n")

#with open("men","w") as f:
 #   f.write(a["hits"])