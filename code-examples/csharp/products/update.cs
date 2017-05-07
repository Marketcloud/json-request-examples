var client = new RestClient("http://api.marketcloud.it/v0/products/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"Weissbier Radler\", \"sku\" : \"C410G90M8BCPJXS4\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);