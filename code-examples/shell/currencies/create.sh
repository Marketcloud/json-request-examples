curl --request POST \
  --url http://api.marketcloud.it/v0/currencies \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Euro","formatting" : "€" }'