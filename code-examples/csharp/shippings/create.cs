var client = new RestClient("http://api.marketcloud.it/v0/shippings");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"ExpressCouriers Inc\",\"price\" : \"€ 5.00\",\"min_price\" : 10.00, \"max_weight\" : 30.00 }", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);