HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/taxes/9")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\": \"Ordinary VAT\"}")
  .asString();