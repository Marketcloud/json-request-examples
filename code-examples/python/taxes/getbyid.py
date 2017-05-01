import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("GET", "/v0/taxes/9", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))