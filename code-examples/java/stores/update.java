HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/stores/3")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"Rocknrolla\"}")
  .asString();