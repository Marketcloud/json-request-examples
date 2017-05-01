import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"access_token\" : \"user-access-token\" ,\"user_id\" : \"the-user-id\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/users/authenticate/facebook", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))