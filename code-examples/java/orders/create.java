HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/orders")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"state\" : \"Processing\",\"total\" : 99.99, \"display_total\" : \"$ 99.99\", \"items_total\" : 89.99, \"dispaly_item_total\" : \"$ 89.99\", \"shipping_address_id\" : 124, \"billing_address_id\" : 123}")
  .asString();