HttpResponse<String> response = Unirest.put("http://api.marketcloud.it/v0/addresses/:id")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"full_name\": \"Jon Snow\",\"country\" : \"Westeros\", \"state\": \"The North\", \"city\": \"the Wall\", \"address1\": \"the Wall, 1\", \"postal_code\": \"54321\"}")
  .asString();