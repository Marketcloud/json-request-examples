curl --request PUT \
  --url http://api.marketcloud.it/v0/carts/9 \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"user_id" : 1,"items" : [{"product_id":13,"quantity":2},{"product_id":15,"quantity":8}]}'