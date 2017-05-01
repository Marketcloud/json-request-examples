HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/categories")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"Brewery\",\"description\" : \"Find the best breweries in the world and taste their amazing beers.\",\"image_url\" : \"http://media.marketcloud.it/v0/\",\"url\" : \"Brewery\"}")
  .asString();