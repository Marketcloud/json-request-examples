HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/users/authenticate/facebook")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"access_token\" : \"user-access-token\" ,\"user_id\" : \"the-user-id\"}")
  .asString();