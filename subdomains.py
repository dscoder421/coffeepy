import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = input("[*] Enter target url: ")

file = open("common.txt", "r")
for line in file:
    word = line.strip()
    full_url = target_url +  