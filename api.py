import requests

url = "https://upcoming-anime.p.rapidapi.com/anime/1"

headers = {
	"X-RapidAPI-Key": "ac4b2b67e6msh85f2775b307ee58p1b5147jsnc4fe82aec600",
	"X-RapidAPI-Host": "upcoming-anime.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())