import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"price\" : \"€ 6.00\", \"max_weight\" : 40.00 }"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/shippings/:id", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))