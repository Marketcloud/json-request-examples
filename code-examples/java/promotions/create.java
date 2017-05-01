HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/promotions")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{  \"name\" : \"Green Friday\",  \"conditions\" : [],  \"effects\" : [{\"type\" : \"CART_VALUE_PERCENTAGE_REDUCTION\",\"value\": 2}]}")
  .asString();