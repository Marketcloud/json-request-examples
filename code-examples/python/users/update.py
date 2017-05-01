import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Jon of the Night's Watch\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/users/3", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))