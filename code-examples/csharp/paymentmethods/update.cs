var client = new RestClient("http://api.marketcloud.it/v0/brands/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"cost_type\" : \"fixed_fee\", \"fixed_fee\" : 5}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);