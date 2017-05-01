curl --request POST \
  --url http://api.marketcloud.it/v0/promotions \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{  "name" : "Green Friday",  "conditions" : [],  "effects" : [{"type" : "CART_VALUE_PERCENTAGE_REDUCTION","value": 2}]}'