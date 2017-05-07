var client = new RestClient("http://api.marketcloud.it/v0/brands");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"name\" : \"Paulaner\",\"description\" : \"Paulaner is a German brewery established in 1634 in Munich.\",\"image_url\" : \"http://media.marketcloud.it/v0/\",\"url\" : \"Paulaner-Beer\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);