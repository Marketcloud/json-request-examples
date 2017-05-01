HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/shippings")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"ExpressCouriers Inc\",\"price\" : \"€ 5.00\",\"min_price\" : 10.00, \"max_weight\" : 30.00 }")
  .asString();