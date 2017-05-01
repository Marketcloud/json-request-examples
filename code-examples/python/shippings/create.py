import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"ExpressCouriers Inc\",\"price\" : \"€ 5.00\",\"min_price\" : 10.00, \"max_weight\" : 30.00 }"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/shippings", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))