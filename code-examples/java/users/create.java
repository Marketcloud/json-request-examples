HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/users")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"email\" : \"jon@snow.wf\",\"name\" : \"Jon Snow\",\"password\" : \"winteriscoming\",\"image_url\" : \"http://media.marketcloud.it/v0/\"}")
  .asString();