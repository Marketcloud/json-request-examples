var client = new RestClient("http://api.marketcloud.it/v0/addresses/:id");
var request = new RestRequest(Method.PUT);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"full_name\": \"Jon Snow\",\"country\" : \"Westeros\", \"state\": \"The North\", \"city\": \"the Wall\", \"address1\": \"the Wall, 1\", \"postal_code\": \"54321\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);