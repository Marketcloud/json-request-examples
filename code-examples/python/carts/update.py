import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"user_id\" : 1,\"items\" : [{\"product_id\":13,\"quantity\":2},{\"product_id\":15,\"quantity\":8}]}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/carts/:id", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))