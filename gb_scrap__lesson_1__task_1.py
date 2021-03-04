import requests

u = 'torvalds'
r = requests.get(f'https://api.github.com/users/{u}/repos')

if r.ok:
    import json
    path = f'{u}.json'
    with open(path, "w") as f:
        json.dump(r.json(), f)
