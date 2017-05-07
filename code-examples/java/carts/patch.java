HttpResponse<String> response = Unirest.patch("http://api.marketcloud.it/v0/carts/:id")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"op\" : \"update\",\"items\" : [{\"product_id\":1,\"quantity\":1}]}")
  .asString();