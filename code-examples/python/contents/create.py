import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"title\" : \"My new blogpost\", \"text\" : \"This is the content of my new blogpost\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/contents", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))