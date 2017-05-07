HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/collections")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{ \"items\" : [ { \"product_id\" : 1  }, { \"product_id\" : 2  }, { \"product_id\" : 3  } ], \"name\" : \"Nerd Stickers\", \"description\" : \"A collection of nerd stickers\"}")
  .asString();