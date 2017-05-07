var client = new RestClient("http://api.marketcloud.it/v0/contents/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"title\" : \"My new blogpost\", \"text\" : \"This is the updated content of my new blogpost\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);