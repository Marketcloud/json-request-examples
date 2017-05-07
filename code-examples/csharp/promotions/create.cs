var client = new RestClient("http://api.marketcloud.it/v0/promotions");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{  \"name\" : \"Green Friday\",  \"conditions\" : [],  \"effects\" : [{\"type\" : \"CART_VALUE_PERCENTAGE_REDUCTION\",\"value\": 2}]}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);