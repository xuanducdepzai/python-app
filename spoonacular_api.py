key = "168135d3ba2e4fc1944d20ec4ad249bf"
base_url = "https://api.spoonacular.com"
import requests

def get_random_recipes(number: int):
    """Get a random recipe"""
    url = f"{base_url}/recipes/random"
    params = {'apiKey': key, 'number': number}
    response = requests.get(url, params=params)
    return response.json()

print(get_random_recipes(1))

def get_recipe_details(recipe_id: int):
    """Get recipe ingredients and instructions"""
    url = f"{base_url}/recipes/{recipe_id}/information"
    params = {'apiKey': key}
    response = requests.get(url, params=params)
    return response.json()
    
def search_recipe(query: str):
    """Search recipes by name"""
    url = f"{base_url}/recipes/complexSearch"
    params = {'apiKey': key, 'query': query, 'number': 10}
    response = requests.get(url, params=params)
    return response.json()
