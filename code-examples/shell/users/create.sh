curl --request POST \
  --url http://api.marketcloud.it/v0/users \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"email" : "jon@snow.wf","name" : "Jon Snow","password" : "winteriscoming","image_url" : "http://media.marketcloud.it/v0/"}'