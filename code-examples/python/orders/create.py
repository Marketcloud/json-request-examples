import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"state\" : \"Processing\",\"total\" : 99.99, \"display_total\" : \"$ 99.99\", \"items_total\" : 89.99, \"dispaly_item_total\" : \"$ 89.99\", \"shipping_address_id\" : 124, \"billing_address_id\" : 123}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/orders", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))