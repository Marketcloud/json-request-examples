import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Hefe-Weissbier\",\"sku\":\"F310R90G8BCPJ1AT\",\"category_id\":\"12\",\"brand_id\":\"19\",\"tax_id\":\"23\",\"store_id\":\"25\",\"description\" : \"The no. 1 Hefe-Weißbier in Germany and one of the world’s favourites.\",\"price\" : \"1.50\",\"stock_level\" : \"1256\",\"published\":\"true\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/products", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))