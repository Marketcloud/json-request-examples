HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/currencies")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"Euro\",\"formatting\" : \"€\" }")
  .asString();