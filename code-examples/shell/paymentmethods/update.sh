curl --request PUT \
  --url http://api.marketcloud.it/v0/brands/:id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"cost_type" : "fixed_fee", "fixed_fee" : 5}'