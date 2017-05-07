var client = new RestClient("http://api.marketcloud.it/v0/contents");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"title\" : \"My new blogpost\", \"text\" : \"This is the content of my new blogpost\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);