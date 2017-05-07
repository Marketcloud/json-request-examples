var client = new RestClient("http://api.marketcloud.it/v0/coupons");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{    \"code\" : \"WELCOME2017\",    \"name\" : \"welcome_2017\",    \"type\" : \"total\",    \"target_type\" : \"CART_COUPON\",    \"discount_type\" : \"NET_REDUCTION\",    \"discount_value\" : 10,    \"active\" : true}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);