curl --request PUT \
  --url http://api.marketcloud.it/v0/brands/3 \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Paulaner Brauerei"}'