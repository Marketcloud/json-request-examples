HttpResponse<String> response = Unirest.delete("http://api.marketcloud.it/v0/addresses/9")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .header("authorization", "YourPublicKey:YourToken")
  .asString();