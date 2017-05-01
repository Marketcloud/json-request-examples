curl --request PATCH \
  --url http://api.marketcloud.it/v0/carts/9 \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"op" : "update","items" : [{"product_id":13,"quantity":20},{"product_id":15,"quantity":18}]}'