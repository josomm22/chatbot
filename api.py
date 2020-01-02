import requests
import json

def catFact():
    data = requests.get('https://catfact.ninja/fact')
    return (data.json()['fact'])

def jokes():
    data = requests.get('https://icanhazdadjoke.com/slack')
    return (data.json()['attachments'][0]['text'])

