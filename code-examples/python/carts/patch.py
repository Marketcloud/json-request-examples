import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"op\" : \"update\",\"items\" : [{\"product_id\":13,\"quantity\":20},{\"product_id\":15,\"quantity\":18}]}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PATCH", "/v0/carts/9", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))