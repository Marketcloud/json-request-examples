HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/coupons/1")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"10PERCENTDISCOUNT\"}")
  .asString();