HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/products/:id/variants/:variant_id")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"price\" : 20}")
  .asString();