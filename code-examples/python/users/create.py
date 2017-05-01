import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"email\" : \"jon@snow.wf\",\"name\" : \"Jon Snow\",\"password\" : \"winteriscoming\",\"image_url\" : \"http://media.marketcloud.it/v0/\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/users", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))