import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"email\" : \"jon@snow.wf\" ,\"password\" : \"winteriscoming\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/users/authenticate", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))