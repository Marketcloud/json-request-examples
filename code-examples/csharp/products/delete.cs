var client = new RestClient("http://api.marketcloud.it/v0/products3");
var request = new RestRequest(Method.DELETE);
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
IRestResponse response = client.Execute(request);