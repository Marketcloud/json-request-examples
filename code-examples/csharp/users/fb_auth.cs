var client = new RestClient("http://api.marketcloud.it/v0/users/authenticate/facebook");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"access_token\" : \"user-access-token\" ,\"user_id\" : \"the-user-id\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);