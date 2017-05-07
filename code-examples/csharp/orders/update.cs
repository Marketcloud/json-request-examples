var client = new RestClient("http://api.marketcloud.it/v0/orders/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"state\" : \"Processing\",\"total\" : 99.99, \"display_total\" : \"$ 99.99\", \"items_total\" : 69.99, \"dispaly_item_total\" : \"$ 69.99\", \"shipping_address_id\" : 123, \"billing_address_id\" : 123}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);