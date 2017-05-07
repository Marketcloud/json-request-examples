import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"email\": \"john@thewall.io\",\"full_name\": \"Jon Snow\",\"country\" : \"Westeros\", \"state\": \"The North\", \"city\": \"Winterfell\", \"address1\": \"Winterfell Castle, 1\", \"postal_code\": \"12345\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/addresses", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))