import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Brewery\",\"description\" : \"Find the best breweries in the world and taste their amazing beers.\",\"image_url\" : \"http://media.marketcloud.it/v0/\",\"url\" : \"Brewery\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/categories", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))