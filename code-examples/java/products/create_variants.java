HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/products/:id/variants")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("[{ \"price\":13.5, \"name\":\"Scala tshirt\", \"description\":\"Tshirt\", \"stock_type\":\"infinite\", \"color\":\"black\", \"size\":\"xl\", \"id\":1}]")
  .asString();