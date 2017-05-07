HttpResponse<String> response = Unirest.delete("http://api.marketcloud.it/v0/currencies/:id")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .header("authorization", "YourPublicKey:YourToken")
  .asString();