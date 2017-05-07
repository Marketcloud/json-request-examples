var client = new RestClient("http://api.marketcloud.it/v0/users/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"Jon of the Night's Watch\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);