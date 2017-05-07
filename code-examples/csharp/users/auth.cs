var client = new RestClient("http://api.marketcloud.it/v0/users/authenticate");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"email\" : \"jon@snow.wf\" ,\"password\" : \"winteriscoming\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);