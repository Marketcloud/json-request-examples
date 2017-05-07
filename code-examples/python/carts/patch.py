import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"op\" : \"update\",\"items\" : [{\"product_id\":1,\"quantity\":1}]}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PATCH", "/v0/carts/:id", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))