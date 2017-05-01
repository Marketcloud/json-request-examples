import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"cost_type\" : \"fixed_fee\", \"fixed_fee\" : 5}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/brands/3", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))