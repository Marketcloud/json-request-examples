import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{    \"code\" : \"WELCOME2017\",    \"name\" : \"welcome_2017\",    \"type\" : \"total\",    \"target_type\" : \"CART_COUPON\",    \"discount_type\" : \"NET_REDUCTION\",    \"discount_value\" : 10,    \"active\" : true}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/coupons", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))