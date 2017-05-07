import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/carts", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))