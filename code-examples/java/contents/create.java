HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/contents")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"title\" : \"My new blogpost\", \"text\" : \"This is the content of my new blogpost\"}")
  .asString();