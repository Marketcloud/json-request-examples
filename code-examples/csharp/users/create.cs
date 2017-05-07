var client = new RestClient("http://api.marketcloud.it/v0/users");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{\"email\" : \"jon@snow.wf\",\"name\" : \"Jon Snow\",\"password\" : \"winteriscoming\",\"image_url\" : \"http://media.marketcloud.it/v0/\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);