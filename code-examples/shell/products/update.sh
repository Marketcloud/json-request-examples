curl --request PUT \
  --url http://api.marketcloud.it/v0/products/1 \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Weissbier Radler", "sku" : "C410G90M8BCPJXS4"}'