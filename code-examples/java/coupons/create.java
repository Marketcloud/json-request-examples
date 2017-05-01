HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/coupons")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{    \"code\" : \"WELCOME2017\",    \"name\" : \"welcome_2017\",    \"type\" : \"total\",    \"target_type\" : \"CART_COUPON\",    \"discount_type\" : \"NET_REDUCTION\",    \"discount_value\" : 10,    \"active\" : true}")
  .asString();