import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"publicKey\" : \"yourPublicKey\",\"secretKey\" : \"yourHashedSecretKey\",\"timestamp\" : 1441724677832}"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/tokens", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))