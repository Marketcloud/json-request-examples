import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{ \"rates\" : [  { \"state\" : \"*\", \"postcode\" : \"*\", \"city\" : \"*\", \"priority\" : 0, \"country\" : \"Italy\", \"rate\" : 22, \"name\" : \"IVA\", \"shipping\" : true, \"country_code\" : \"IT\" } ], \"name\" : \"Standard VAT\", \"application_id\" : 4323, \"id\" : 169405 }"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/taxes", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))