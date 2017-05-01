import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"full_name\": \"Jon Snow\",\"country\" : \"Westeros\", \"state\": \"The North\", \"city\": \"the Wall\", \"address1\": \"the Wall, 1\", \"postal_code\": \"54321\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("PUT", "/v0/addresses/9", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))