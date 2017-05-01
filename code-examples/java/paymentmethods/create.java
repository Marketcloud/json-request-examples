HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/paymentMethods")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"name\" : \"Bank deposit\",\"description\" : \"Payment through bank deposit.\",\"cost_type\" : \"no_cost\", \"active\":true}")
  .asString();