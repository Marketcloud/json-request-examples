HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/carts/9")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"user_id\" : 1,\"items\" : [{\"product_id\":13,\"quantity\":2},{\"product_id\":15,\"quantity\":8}]}")
  .asString();