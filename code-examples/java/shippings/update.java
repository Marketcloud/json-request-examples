HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/shippings/:id")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"price\" : \"€ 6.00\", \"max_weight\" : 40.00 }")
  .asString();