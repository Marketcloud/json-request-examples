curl --request POST \
  --url http://api.marketcloud.it/v0/users/authenticate/facebook \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"access_token" : "user-access-token" ,"user_id" : "the-user-id"}'