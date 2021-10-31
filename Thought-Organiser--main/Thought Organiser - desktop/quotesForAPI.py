import requests

def return_API_qoute():
    response = requests.get('https://api.quotable.io/random')
    return response.json()['content'],"\n - "+response.json()['author']

