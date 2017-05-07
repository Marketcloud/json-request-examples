HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/users/:id")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"Jon of the Night's Watch\"}")
  .asString();