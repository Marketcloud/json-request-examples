curl --request POST \
  --url http://api.marketcloud.it/v0/collections \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{ "items" : [ { "product_id" : 1  }, { "product_id" : 2  }, { "product_id" : 3  } ], "name" : "Nerd Stickers", "description" : "A collection of nerd stickers"}'