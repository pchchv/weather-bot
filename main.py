import requests


def req(city):
    url = 'http://localhost:8080/stats?city=' + city
    res = requests.get(url)
    return res.text
