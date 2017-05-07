HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/carts")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{}")
  .asString();