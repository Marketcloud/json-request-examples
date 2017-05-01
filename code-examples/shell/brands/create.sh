curl --request POST \
  --url http://api.marketcloud.it/v0/brands \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Paulaner","description" : "Paulaner is a German brewery established in 1634 in Munich.","image_url" : "http://media.marketcloud.it/v0/","url" : "Paulaner-Beer"}'