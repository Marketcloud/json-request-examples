curl --request POST \
  --url http://api.marketcloud.it/v0/products \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{"name" : "Hefe-Weissbier","sku":"F310R90G8BCPJ1AT","category_id":"12","brand_id":"19","tax_id":"23","store_id":"25","description" : "The no. 1 Hefe-Weißbier in Germany and one of the world’s favourites.","price" : "1.50","stock_level" : "1256","published":"true"}'