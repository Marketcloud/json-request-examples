curl --request PUT \
  --url http://api.marketcloud.it/v0/users/:id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Jon of the Night'\''s Watch"}'