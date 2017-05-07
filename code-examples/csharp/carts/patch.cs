var client = new RestClient("http://api.marketcloud.it/v0/carts/:id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"op\" : \"update\",\"items\" : [{\"product_id\":1,\"quantity\":1}]}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);