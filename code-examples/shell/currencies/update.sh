curl --request PUT \
  --url http://api.marketcloud.it/v0/currencies/:id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "American Dollar","formatting" : "$" }'