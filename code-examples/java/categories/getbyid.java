HttpResponse<String> response = Unirest.get("http://api.marketcloud.it/v0/categories/9")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .asString();