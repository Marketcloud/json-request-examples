HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/taxes")
  .header("authorization", "YourPublicKey:YourToken")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{ \"rates\" : [  { \"state\" : \"*\", \"postcode\" : \"*\", \"city\" : \"*\", \"priority\" : 0, \"country\" : \"Italy\", \"rate\" : 22, \"name\" : \"IVA\", \"shipping\" : true, \"country_code\" : \"IT\" } ], \"name\" : \"Standard VAT\", \"application_id\" : 4323, \"id\" : 169405 }")
  .asString();