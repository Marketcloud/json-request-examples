import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Euro\",\"formatting\" : \"€\" }"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/currencies", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))