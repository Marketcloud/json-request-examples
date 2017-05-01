curl --request POST \
  --url http://api.marketcloud.it/v0/tokens \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"publicKey" : "yourPublicKey","secretKey" : "yourHashedSecretKey","timestamp" : 1441724677832}'