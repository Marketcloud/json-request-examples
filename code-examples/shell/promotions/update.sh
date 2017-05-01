curl --request PUT \
  --url http://api.marketcloud.it/v0/promotions/1 \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Black Saturday"}'