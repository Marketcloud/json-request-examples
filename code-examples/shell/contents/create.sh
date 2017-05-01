curl --request POST \
  --url http://api.marketcloud.it/v0/contents \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"title" : "My new blogpost", "text" : "This is the content of my new blogpost"}'