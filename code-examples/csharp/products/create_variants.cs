var client = new RestClient("http://api.marketcloud.it/v0/products/:id/variants");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "[{ \"price\":13.5, \"name\":\"Scala tshirt\", \"description\":\"Tshirt\", \"stock_type\":\"infinite\", \"color\":\"black\", \"size\":\"xl\", \"id\":1}]", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);