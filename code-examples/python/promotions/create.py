import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{  \"name\" : \"Green Friday\",  \"conditions\" : [],  \"effects\" : [{\"type\" : \"CART_VALUE_PERCENTAGE_REDUCTION\",\"value\": 2}]}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/promotions", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))