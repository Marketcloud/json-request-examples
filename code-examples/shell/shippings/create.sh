curl --request POST \
  --url http://api.marketcloud.it/v0/shippings \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "ExpressCouriers Inc","price" : "€ 5.00","min_price" : 10.00, "max_weight" : 30.00 }'