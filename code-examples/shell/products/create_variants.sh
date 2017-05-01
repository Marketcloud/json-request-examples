curl --request POST \
  --url http://api.marketcloud.it/v0/products/:id/variants \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '[{ "price":13.5, "name":"Scala tshirt", "description":"Tshirt", "stock_type":"infinite", "color":"black", "size":"xl", "id":1}]'