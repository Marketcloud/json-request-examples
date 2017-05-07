var client = new RestClient("http://api.marketcloud.it/v0/promotions/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"Black Saturday\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);