import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"title\" : \"My new blogpost\", \"text\" : \"This is the updated content of my new blogpost\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/contents/:id", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))