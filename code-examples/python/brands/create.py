import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Paulaner\",\"description\" : \"Paulaner is a German brewery established in 1634 in Munich.\",\"image_url\" : \"http://media.marketcloud.it/v0/\",\"url\" : \"Paulaner-Beer\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/brands", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))