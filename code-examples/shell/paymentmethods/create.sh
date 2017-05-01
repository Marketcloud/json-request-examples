curl --request POST \
  --url http://api.marketcloud.it/v0/paymentMethods \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Bank deposit","description" : "Payment through bank deposit.","cost_type" : "no_cost", "active":true}'