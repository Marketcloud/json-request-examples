var client = new RestClient("http://api.marketcloud.it/v0/collections");
var request = new RestRequest(Method.POST);
request.AddHeader("content-type", "application/json");
request.AddHeader("accept", "application/json");
request.AddHeader("authorization", "YourPublicKey:YourToken");
request.AddParameter("application/json", "{ \"items\" : [ { \"product_id\" : 1  }, { \"product_id\" : 2  }, { \"product_id\" : 3  } ], \"name\" : \"Nerd Stickers\", \"description\" : \"A collection of nerd stickers\"}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);