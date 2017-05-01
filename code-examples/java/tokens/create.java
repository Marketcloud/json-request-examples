HttpResponse<String> response = Unirest.post("http://api.marketcloud.it/v0/tokens")
  .header("accept", "application/json")
  .header("content-type", "application/json")
  .body("{\"publicKey\" : \"yourPublicKey\",\"secretKey\" : \"yourHashedSecretKey\",\"timestamp\" : 1441724677832}")
  .asString();