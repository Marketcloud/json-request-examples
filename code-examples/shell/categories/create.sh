curl --request POST \
  --url http://api.marketcloud.it/v0/categories \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Brewery","description" : "Find the best breweries in the world and taste their amazing beers.","image_url" : "http://media.marketcloud.it/v0/","url" : "Brewery"}'