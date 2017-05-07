HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/contents/:id")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"title\" : \"My new blogpost\", \"text\" : \"This is the updated content of my new blogpost\"}")
  .asString();