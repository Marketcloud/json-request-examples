var client = new RestClient("http://api.marketcloud.it/v0/tokens");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddParameter("application/json", "{\"publicKey\" : \"yourPublicKey\",\"secretKey\" : \"yourHashedSecretKey\",\"timestamp\" : 1441724677832}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);