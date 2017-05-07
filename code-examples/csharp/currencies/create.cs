var client = new RestClient("http://api.marketcloud.it/v0/currencies");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"Euro\",\"formatting\" : \"€\" }", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);