var client = new RestClient("http://api.marketcloud.it/v0/users");
var request = new RestRequest(Method.GET);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
IRestResponse response = client.Execute(request);