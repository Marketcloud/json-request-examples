import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "YourPublicKey:YourToken"
    }

conn.request("DELETE", "/v0/contents/2", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))