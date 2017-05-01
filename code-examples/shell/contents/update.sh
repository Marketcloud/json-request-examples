curl --request PUT \
  --url http://api.marketcloud.it/v0/contents/3 \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"title" : "My new blogpost", "text" : "This is the updated content of my new blogpost"}'