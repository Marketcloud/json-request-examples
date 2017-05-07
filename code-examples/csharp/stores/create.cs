var client = new RestClient("http://api.marketcloud.it/v0/stores");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"The Beer Shop\",\"owner_email\" : \"thebeer@shop.com\",\"description\" : \"The Beer Shop is the coolest shop ever. Come every week to taste our always new beer!\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);