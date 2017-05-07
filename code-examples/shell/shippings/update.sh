curl --request PUT \
  --url http://api.marketcloud.it/v0/shippings/:id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"price" : "€ 6.00", "max_weight" : 40.00 }'