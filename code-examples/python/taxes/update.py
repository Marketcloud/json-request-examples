import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\": \"Ordinary VAT\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/taxes/:id", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))