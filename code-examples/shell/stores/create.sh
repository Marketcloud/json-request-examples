curl --request POST \
  --url http://api.marketcloud.it/v0/stores \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "The Beer Shop","owner_email" : "thebeer@shop.com","description" : "The Beer Shop is the coolest shop ever. Come every week to taste our always new beer!"}'