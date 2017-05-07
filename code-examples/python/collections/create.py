import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{ \"items\" : [ { \"product_id\" : 1  }, { \"product_id\" : 2  }, { \"product_id\" : 3  } ], \"name\" : \"Nerd Stickers\", \"description\" : \"A collection of nerd stickers\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/collections", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))