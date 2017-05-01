import http.client

conn = http.client.HTTPConnection("api.marketcloud.it")

payload = "{\"name\" : \"Test Image\",\"filename\":\"test_image.gif\",\"description\" : \"A very simple test image\",\"file\" : \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7\"}"

headers = {
    'authorization': "YourPublicKey:YourToken",
    'content-type': "application/json"
    }

conn.request("POST", "/v0/files", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))