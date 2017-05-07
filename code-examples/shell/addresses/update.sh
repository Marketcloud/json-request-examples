curl --request PUT \
  --url http://api.marketcloud.it/v0/addresses/:id \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"full_name": "Jon Snow","country" : "Westeros", "state": "The North", "city": "the Wall", "address1": "the Wall, 1", "postal_code": "54321"}'