package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.marketcloud.it/v0/coupons"

	payload := strings.NewReader("{    \"code\" : \"WELCOME2017\",    \"name\" : \"welcome_2017\",    \"type\" : \"total\",    \"target_type\" : \"CART_COUPON\",    \"discount_type\" : \"NET_REDUCTION\",    \"discount_value\" : 10,    \"active\" : true}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("authorization", "YourPublicKey:YourToken")
	req.Header.Add("accept", "application/json")
	req.Header.Add("content-type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}