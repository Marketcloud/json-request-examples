HttpResponse<String> response = Unirest.patch("http://api.marketcloud.it/v0/carts/9")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"op\" : \"update\",\"items\" : [{\"product_id\":13,\"quantity\":20},{\"product_id\":15,\"quantity\":18}]}")
  .asString();