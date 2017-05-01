HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/products/1")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"Weissbier Radler\", \"sku\" : \"C410G90M8BCPJXS4\"}")
  .asString();