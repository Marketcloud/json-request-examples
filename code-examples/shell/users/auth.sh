curl --request POST \
  --url http://api.marketcloud.it/v0/users/authenticate \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"email" : "jon@snow.wf" ,"password" : "winteriscoming"}'