import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "[{ \"price\":13.5, \"name\":\"Scala tshirt\", \"description\":\"Tshirt\", \"stock_type\":\"infinite\", \"color\":\"black\", \"size\":\"xl\", \"id\":1}]"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/products/:id/variants", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))