curl --request PUT \
  --url http://api.marketcloud.it/v0/categories/:id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Wine Company"}'