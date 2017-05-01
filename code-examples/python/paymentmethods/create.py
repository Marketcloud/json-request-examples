import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Bank deposit\",\"description\" : \"Payment through bank deposit.\",\"cost_type\" : \"no_cost\", \"active\":true}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/paymentMethods", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))