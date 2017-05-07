var client = new RestClient("http://api.marketcloud.it/v0/orders");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"state\" : \"Processing\",\"total\" : 99.99, \"display_total\" : \"$ 99.99\", \"items_total\" : 89.99, \"dispaly_item_total\" : \"$ 89.99\", \"shipping_address_id\" : 124, \"billing_address_id\" : 123}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);