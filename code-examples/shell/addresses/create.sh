curl --request POST \
  --url http://api.marketcloud.it/v0/addresses \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"email": "john@thewall.io","full_name": "Jon Snow","country" : "Westeros", "state": "The North", "city": "Winterfell", "address1": "Winterfell Castle, 1", "postal_code": "12345"}'