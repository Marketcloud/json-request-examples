var client = new RestClient("http://api.marketcloud.it/v0/paymentMethods");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"Bank deposit\",\"description\" : \"Payment through bank deposit.\",\"cost_type\" : \"no_cost\", \"active\":true}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);