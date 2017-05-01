import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"price\" : 20}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/products/:id/variants/:variant_id", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))