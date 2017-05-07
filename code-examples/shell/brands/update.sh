curl --request PUT \
  --url http://api.marketcloud.it/v0/brands/%7Bid%7D \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Paulaner Brauerei"}'