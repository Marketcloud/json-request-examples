var client = new RestClient("http://api.marketcloud.it/v0/shippings/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"price\" : \"€ 6.00\", \"max_weight\" : 40.00 }", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);