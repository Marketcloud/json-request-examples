curl --request PUT \
  --url http://api.marketcloud.it/v0/products/:id/variants/:variant_id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"price" : 20}'