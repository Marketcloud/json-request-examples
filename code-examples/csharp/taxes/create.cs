var client = new RestClient("http://api.marketcloud.it/v0/taxes");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{ \"rates\" : [  { \"state\" : \"*\", \"postcode\" : \"*\", \"city\" : \"*\", \"priority\" : 0, \"country\" : \"Italy\", \"rate\" : 22, \"name\" : \"IVA\", \"shipping\" : true, \"country_code\" : \"IT\" } ], \"name\" : \"Standard VAT\", \"application_id\" : 4323, \"id\" : 169405 }", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);