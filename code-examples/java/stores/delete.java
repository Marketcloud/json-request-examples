HttpResponse<String> response = Unirest.delete("http://api.marketcloud.it/v0/stores/2")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .header("authorization", "YourPublicKey:YourToken")
  .asString();