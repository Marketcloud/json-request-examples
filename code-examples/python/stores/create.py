import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"The Beer Shop\",\"owner_email\" : \"thebeer@shop.com\",\"description\" : \"The Beer Shop is the coolest shop ever. Come every week to taste our always new beer!\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/stores", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))