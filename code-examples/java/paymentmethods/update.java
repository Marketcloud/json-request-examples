HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/brands/:id")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"cost_type\" : \"fixed_fee\", \"fixed_fee\" : 5}")
  .asString();