curl --request PATCH \
  --url http://api.marketcloud.it/v0/carts/:id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"op" : "update","items" : [{"product_id":1,"quantity":1}]}'