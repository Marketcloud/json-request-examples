var client = new RestClient("http://api.marketcloud.it/v0/carts/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"user_id\" : 1,\"items\" : [{\"product_id\":13,\"quantity\":2},{\"product_id\":15,\"quantity\":8}]}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);