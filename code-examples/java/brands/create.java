HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/brands")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"Paulaner\",\"description\" : \"Paulaner is a German brewery established in 1634 in Munich.\",\"image_url\" : \"http://media.marketcloud.it/v0/\",\"url\" : \"Paulaner-Beer\"}")
  .asString();