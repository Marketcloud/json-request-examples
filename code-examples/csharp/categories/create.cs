var client = new RestClient("http://api.marketcloud.it/v0/categories");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"Brewery\",\"description\" : \"Find the best breweries in the world and taste their amazing beers.\",\"image_url\" : \"http://media.marketcloud.it/v0/\",\"url\" : \"Brewery\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);