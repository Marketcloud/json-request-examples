var client = new RestClient("http://api.marketcloud.it/v0/addresses");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"email\": \"john@thewall.io\",\"full_name\": \"Jon Snow\",\"country\" : \"Westeros\", \"state\": \"The North\", \"city\": \"Winterfell\", \"address1\": \"Winterfell Castle, 1\", \"postal_code\": \"12345\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);