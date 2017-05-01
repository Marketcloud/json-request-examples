HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/users/authenticate")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"email\" : \"jon@snow.wf\" ,\"password\" : \"winteriscoming\"}")
  .asString();