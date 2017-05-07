import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Weissbier Radler\", \"sku\" : \"C410G90M8BCPJXS4\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/products/:id", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))