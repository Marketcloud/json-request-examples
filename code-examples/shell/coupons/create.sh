curl --request POST \
  --url http://api.marketcloud.it/v0/coupons \
  --header 'accept: application/json' \
  --header 'authorization: YourPublicKey:YourToken' \
  --header 'content-type: application/json' \
  --data '{    "code" : "WELCOME2017",    "name" : "welcome_2017",    "type" : "total",    "target_type" : "CART_COUPON",    "discount_type" : "NET_REDUCTION",    "discount_value" : 10,    "active" : true}'