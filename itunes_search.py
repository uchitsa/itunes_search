import requests


def search(term, media):
    url = "https://itunes.apple.com/search"
    payload = {"term": term, "media":media}
    response = requests.get(url, params = payload)
    response.raise_for_status()
    results = response.json().get("results", [])
    return results
    

print("Search in iTunes catalogs with API.")
print("Input term:")    
term = input()   
print("Input media:")    
media = input()
print(search(term, media))
