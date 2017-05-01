HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/stores")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"The Beer Shop\",\"owner_email\" : \"thebeer@shop.com\",\"description\" : \"The Beer Shop is the coolest shop ever. Come every week to taste our always new beer!\"}")
  .asString();