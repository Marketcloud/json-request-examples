HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/addresses")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"full_name\": \"Jon Snow\",\"country\" : \"Westeros\", \"state\": \"The North\", \"city\": \"Winterfell\", \"address1\": \"Winterfell Castle, 1\", \"postal_code\": \"12345\"}")
  .asString();