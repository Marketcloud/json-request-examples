curl --request POST \
  --url http://api.marketcloud.it/v0/orders \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"state" : "Processing","total" : 99.99, "display_total" : "$ 99.99", "items_total" : 89.99, "dispaly_item_total" : "$ 89.99", "shipping_address_id" : 124, "billing_address_id" : 123}'