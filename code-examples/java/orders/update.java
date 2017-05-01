HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/orders/9")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"state\" : \"Processing\",\"total\" : 99.99, \"display_total\" : \"$ 99.99\", \"items_total\" : 69.99, \"dispaly_item_total\" : \"$ 69.99\", \"shipping_address_id\" : 123, \"billing_address_id\" : 123}")
  .asString();